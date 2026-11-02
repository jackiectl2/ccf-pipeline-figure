#!/usr/bin/env python3
"""Inspect and atomically reserve isolated figure-run directories."""

import argparse
import json
import re
from pathlib import Path


SUFFIX = {"numbered_regions": "numbered", "topology_first": "flexible"}
PROFILE_RE = re.compile(r"composition_profile\s*[:=]\s*[`\"']?(numbered_regions|topology_first)")


def normalize_slug(value):
    slug = value.strip().lower().replace("_", "-")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        raise ValueError("figure slug must contain lowercase letters, digits, and hyphens")
    return slug


def runs_root(project):
    return project / "output" / "imagegen" / project.name


def legacy_profile(directory):
    for name in ("SELECTED.md", "v01.review.md"):
        path = directory / name
        if path.is_file():
            try:
                with path.open(encoding="utf-8") as source:
                    header = source.read(8192)
            except (OSError, UnicodeError):
                continue
            match = PROFILE_RE.search(header)
            if match:
                return match.group(1)
    return None


def inspect_runs(project, figure_slug):
    slug = normalize_slug(figure_slug)
    root = runs_root(project)
    found = []
    if not root.is_dir():
        return found
    for directory in sorted(root.iterdir()):
        if not directory.is_dir():
            continue
        manifest = directory / "RUN.json"
        if manifest.is_file():
            try:
                data = json.loads(manifest.read_text(encoding="utf-8"))
            except (ValueError, OSError):
                data = {}
            if data.get("figure_slug") != slug:
                continue
            profile = data.get("composition_profile")
            if profile not in SUFFIX:
                profile = None
            found.append({"path": str(directory), "profile": profile, "legacy": False})
            continue
        name = directory.name.lower().replace("_", "-")
        match = re.fullmatch(rf"{re.escape(slug)}-(numbered|flexible)(?:-\d+)?", name)
        if name != slug and not match:
            continue
        profile = legacy_profile(directory)
        if profile is None and match:
            profile = "numbered_regions" if match.group(1) == "numbered" else "topology_first"
        found.append({"path": str(directory), "profile": profile, "legacy": True})
    return found


def inspect_project(project):
    """List run metadata across the project without opening figure content."""
    root = runs_root(project)
    found = []
    if not root.is_dir():
        return found
    for directory in sorted(root.iterdir()):
        if not directory.is_dir():
            continue
        manifest = directory / "RUN.json"
        if manifest.is_file():
            try:
                data = json.loads(manifest.read_text(encoding="utf-8"))
            except (ValueError, OSError):
                data = {}
            found.append({"path": str(directory), "figure_slug": data.get("figure_slug"),
                          "profile": data.get("composition_profile"), "legacy": False})
            continue
        if not ((directory / "SELECTED.md").is_file() or (directory / "v01.png").is_file()):
            continue
        name = directory.name.lower().replace("_", "-")
        match = re.fullmatch(r"(.+?)-(numbered|flexible)(?:-\d+)?", name)
        slug = match.group(1) if match else name
        profile = legacy_profile(directory)
        if profile is None and match:
            profile = "numbered_regions" if match.group(2) == "numbered" else "topology_first"
        found.append({"path": str(directory), "figure_slug": slug,
                      "profile": profile, "legacy": True})
    return found


def reserve(project, figure_slug, profile, new_run=False):
    if profile not in SUFFIX:
        raise ValueError(f"unknown composition profile: {profile}")
    if not project.is_dir():
        raise ValueError(f"project folder does not exist: {project}")
    slug = normalize_slug(figure_slug)
    found = inspect_runs(project, slug)
    same = [item for item in found if item["profile"] == profile]
    unknown = [item for item in found if item["profile"] is None]
    if (same or unknown) and not new_run:
        return {"status": "existing_run", "figure_slug": slug, "profile": profile,
                "same_profile": same, "unclassified": unknown}

    root = runs_root(project)
    root.mkdir(parents=True, exist_ok=True)
    base = f"{slug}-{SUFFIX[profile]}"
    index = 1
    while True:
        name = base if index == 1 else f"{base}-{index:02d}"
        directory = root / name
        try:
            directory.mkdir()
        except FileExistsError:
            if not new_run:
                return {"status": "existing_run", "figure_slug": slug, "profile": profile,
                        "same_profile": inspect_runs(project, slug), "unclassified": []}
            index += 1
            continue
        manifest = {"schema_version": 1, "figure_slug": slug,
                    "composition_profile": profile, "run_index": index}
        (directory / "RUN.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        return {"status": "reserved", "run_dir": str(directory), **manifest}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("inspect", "reserve"))
    parser.add_argument("--project", type=Path, required=True)
    parser.add_argument("--figure", required=True, help="Stable slug for the figure's scientific purpose")
    parser.add_argument("--profile", choices=tuple(SUFFIX), required=True)
    parser.add_argument("--new-run", action="store_true", help="Use only after an explicit fresh-repeat request")
    args = parser.parse_args()
    if args.new_run and args.action != "reserve":
        parser.error("--new-run requires reserve")
    try:
        result = ({"status": "inspected", "runs": inspect_project(args.project),
                   "matching_slug": inspect_runs(args.project, args.figure)}
                  if args.action == "inspect" else
                  reserve(args.project, args.figure, args.profile, args.new_run))
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 2 if result["status"] == "existing_run" else 0


if __name__ == "__main__":
    raise SystemExit(main())
