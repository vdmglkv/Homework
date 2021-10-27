import unittest
from datetime import date
from RP import console_args


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
