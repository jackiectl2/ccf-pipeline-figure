import tempfile
import unittest
from pathlib import Path
from export_vector import inspect_svg


class SVGPreflightTests(unittest.TestCase):
    def inspect(self, body, expected=None):
        with tempfile.TemporaryDirectory() as folder:
            svg = Path(folder) / 'input.svg'
            svg.write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
                           '<rect x="0" y="0" width="100" height="100" fill="white"/>'
                           + body + '</svg>', encoding='utf-8')
            return inspect_svg(svg, expected or ['ŷ ≤ σ'], {'TestFont'})

    def test_live_unicode_text(self):
        result = self.inspect('<text x="10" y="20" font-family="TestFont" font-size="10">ŷ ≤ σ</text>')
        self.assertEqual(result[0], ['ŷ ≤ σ'])
        self.assertEqual(result[1], 1)

    def test_raster_wrapper_rejected(self):
        with self.assertRaises(ValueError):
            self.inspect('<image href="source.png"/>')

    def test_path_only_rejected(self):
        with self.assertRaises(ValueError):
            self.inspect('<path d="M0,0 L10,10"/>')

    def test_invisible_text_rejected(self):
        with self.assertRaises(ValueError):
            self.inspect('<text font-family="TestFont" font-size="10" opacity="0">ŷ ≤ σ</text>')

    def test_missing_duplicate_label_rejected(self):
        with self.assertRaises(ValueError):
            self.inspect('<text font-family="TestFont" font-size="10">ŷ ≤ σ</text>', ['ŷ ≤ σ', 'ŷ ≤ σ'])

    def test_unregistered_font_rejected(self):
        with self.assertRaises(ValueError):
            self.inspect('<text font-family="Unknown" font-size="10">ŷ ≤ σ</text>')


if __name__ == '__main__':
    unittest.main()
