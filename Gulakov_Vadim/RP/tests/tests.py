import unittest
# from RP.converter import create_html, create_pdf
from Gulakov_Vadim.RP import console_args


class TestParser(unittest.TestCase):
    """

    """

    def test_parse_args(self):
        """Test to assert that command-line input is parsed correctly."""
        args = console_args.args
        self.assertEqual(args.json, False)
        self.assertEqual(args.verbose, False)
        self.assertIsNone(args.date)
        self.assertEqual(args.clear, False)
        self.assertEqual(args.limit, 1)
        self.assertIsNone(args.html)
        self.assertIsNone(args.pdf)
        self.assertEqual(args.source, "https://news.yahoo.com/rss/")

    def test_create_table(self):
        pass

    def test_save_html_file(self):
        pass

    def test_save_pdf_file(self):
        pass


