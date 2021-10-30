import argparse
import os
import unittest
from RP import console_args, db
from unittest.mock import patch


class TestParser(unittest.TestCase):

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
        self.assertTrue(db.create_table())

    @patch("logging.warning")
    @patch("argparse.ArgumentParser.parse_args",
           return_value=argparse.Namespace(clear=True))
    def test_clear_cache(self, moack, moack2):
        if os.path.exists(db.CACHE):
            self.assertTrue(db.clear_cache())

    def test_get_data_from_cache(self):
        args = console_args.args
        self.assertIsNone(db.get_data(args.source, args.date, args.limit))
