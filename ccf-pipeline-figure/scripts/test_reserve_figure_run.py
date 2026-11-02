import json
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from reserve_figure_run import inspect_project, inspect_runs, reserve, runs_root


class FigureRunIsolationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.project = Path(self.temporary.name) / "Research_Project"
        self.project.mkdir()

    def test_opposite_profiles_get_independent_briefs_and_version_spaces(self):
        flexible = reserve(self.project, "method-overview", "topology_first")
        numbered = reserve(self.project, "method-overview", "numbered_regions")
        self.assertEqual(flexible["status"], "reserved")
        self.assertEqual(numbered["status"], "reserved")
        self.assertNotEqual(flexible["run_dir"], numbered["run_dir"])
        self.assertTrue(flexible["run_dir"].endswith("method-overview-flexible"))
        self.assertTrue(numbered["run_dir"].endswith("method-overview-numbered"))
        for result in (flexible, numbered):
            run = Path(result["run_dir"])
            self.assertEqual(json.loads((run / "RUN.json").read_text())["composition_profile"],
                             result["composition_profile"])
            self.assertFalse((run / "v01.png").exists())
        self.assertFalse((self.project / "TECHNICAL_FIGURE_BRIEF.md").exists())

    def test_repeat_requires_explicit_new_run_and_does_not_append(self):
        first = reserve(self.project, "method-overview", "topology_first")
        duplicate = reserve(self.project, "method-overview", "topology_first")
        second = reserve(self.project, "method-overview", "topology_first", new_run=True)
        self.assertEqual(duplicate["status"], "existing_run")
        self.assertEqual(second["status"], "reserved")
        self.assertTrue(second["run_dir"].endswith("method-overview-flexible-02"))
        self.assertEqual(len(inspect_runs(self.project, "method-overview")), 2)
        self.assertTrue(Path(first["run_dir"]).is_dir())

    def test_concurrent_same_profile_claims_cannot_share_a_run(self):
        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(lambda _: reserve(self.project, "method-overview",
                                                      "numbered_regions"), range(2)))
        self.assertEqual(sorted(item["status"] for item in results),
                         ["existing_run", "reserved"])
        self.assertEqual(len(list(runs_root(self.project).iterdir())), 1)

    def test_unclassified_legacy_run_requires_review_without_reading_images(self):
        legacy = runs_root(self.project) / "method_overview"
        legacy.mkdir(parents=True)
        (legacy / "v01.png").write_bytes(b"not a real image")
        result = reserve(self.project, "method-overview", "topology_first")
        self.assertEqual(result["status"], "existing_run")
        self.assertEqual(result["unclassified"][0]["path"], str(legacy))
        self.assertFalse((runs_root(self.project) / "method-overview-flexible").exists())

    def test_known_legacy_opposite_profile_does_not_block(self):
        legacy = runs_root(self.project) / "method_overview_numbered"
        legacy.mkdir(parents=True)
        (legacy / "v01.review.md").write_text("composition_profile: numbered_regions\n")
        (legacy / "v01.png").write_bytes(b"not a real image")
        result = reserve(self.project, "method-overview", "topology_first")
        self.assertEqual(result["status"], "reserved")
        self.assertTrue(result["run_dir"].endswith("method-overview-flexible"))
        self.assertEqual({item["profile"] for item in inspect_project(self.project)},
                         {"numbered_regions", "topology_first"})


if __name__ == "__main__":
    unittest.main()
