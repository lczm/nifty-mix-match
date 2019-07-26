# This file is mainly for testing purposes
# Advised to run once in a while / after adding a new feature
import os
import unittest

class TestScraper(unittest.TestCase):

    def test_links_exist(self):
        self.assertTrue(os.path.isfile('./links.csv'))

    def test_paths_exist(self):
        self.assertTrue(os.path.isfile('./paths.csv'))

    def test_app_exist(self):
        self.assertTrue(os.path.isfile('./app.py'))


if __name__ == "__main__":
    unittest.main()

