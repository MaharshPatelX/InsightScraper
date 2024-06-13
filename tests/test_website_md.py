import unittest
from src.scraper.website_md import fetch_page_content, generate_filename

class TestWebsiteMD(unittest.TestCase):
    def test_fetch_page_content(self):
        # Add test for fetch_page_content function
        pass

    def test_generate_filename(self):
        self.assertEqual(generate_filename("https://example.com/test"), "https%3A__example.com_test.md")

if __name__ == '__main__':
    unittest.main()
