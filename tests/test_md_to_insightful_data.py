import unittest
from src.insights.md_to_insightful_data import prompt_splitter

class TestMDToInsightfulData(unittest.TestCase):
    def test_prompt_splitter(self):
        result = prompt_splitter("a" * 40000)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], "a" * 20000)
        self.assertEqual(result[1], "a" * 20000)

if __name__ == '__main__':
    unittest.main()
