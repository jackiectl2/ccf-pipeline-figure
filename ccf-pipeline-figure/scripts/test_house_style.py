"""Test local layout primitives without loading or invoking Figure Smith."""
import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch


spec = importlib.util.spec_from_file_location(
    "pipeline_house_style", Path(__file__).resolve().parents[1] / "assets/house_style.py")
house_style = importlib.util.module_from_spec(spec)
spec.loader.exec_module(house_style)


class LayoutTests(unittest.TestCase):
    def setUp(self):
        self.backend_guard = patch.object(
            house_style, "figuresmith", side_effect=AssertionError("disabled backend called"))
        self.backend_guard.start()
        self.addCleanup(self.backend_guard.stop)
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.figure = house_style.Figure.__new__(house_style.Figure)
        self.figure.fs = SimpleNamespace(
            OUT=Path(folder.name), FONT_LABEL=10, FONT_SMALL=8, TEXT_W_PT=100)
        self.figure.name = "test-layout"
        self.figure.w = self.figure.h = 1000
        self.figure.frac = 1.0
        self.figure.dia = SimpleNamespace(node=Mock(), write=Mock())
        self.figure.geo = house_style._Geo(1000, 1000)
        self.figure._regions = []

    def write(self):
        with contextlib.redirect_stdout(io.StringIO()):
            return self.figure.write()

    def test_no_region_count_quota(self):
        for count in (0, 1, 2, 4, 7):
            with self.subTest(count=count):
                self.figure._regions = [f"group {n}" for n in range(count)]
                self.figure.dia.write.reset_mock()
                self.assertEqual(self.write(), self.figure.fs.OUT / "test-layout.drawio")
                self.figure.dia.write.assert_called_once()

    def test_unnumbered_region_omits_badge_and_reclaims_title_space(self):
        for badge in (None, ""):
            with self.subTest(badge=badge):
                self.figure.geo = house_style._Geo(1000, 1000)
                self.figure.region(10, 10, 400, 150, badge, "Shared memory")
                names = [item[4] for item in self.figure.geo.all]
                self.assertFalse(any(name.startswith("badge:") for name in names))
                title = next(item for item in self.figure.geo.all
                             if item[4] == "banner:Shared memory")
                self.assertLess(title[0], 10 + 15 * 1.7)
                self.assertGreater(title[2], 400 - 15 * 2.4)
                self.figure.geo.check("unnumbered")

    def test_explicit_badge_is_retained(self):
        self.figure.region(10, 10, 400, 150, "1", "Encode")
        self.assertIn("badge:1", [item[4] for item in self.figure.geo.all])
        self.figure.geo.check("numbered")

    def test_overflow_still_rejected_without_regions(self):
        self.figure.geo.add(990, 10, 30, 30, "label")
        with self.assertRaisesRegex(SystemExit, "canvas"):
            self.write()
        self.figure.dia.write.assert_not_called()

    def test_overlap_still_rejected_without_regions(self):
        self.figure.geo.add(10, 10, 30, 30, "icon")
        self.figure.geo.add(20, 20, 30, 30, "label")
        with self.assertRaisesRegex(SystemExit, "overlap"):
            self.write()
        self.figure.dia.write.assert_not_called()


if __name__ == "__main__":
    unittest.main()
