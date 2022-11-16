import unittest
from helper.main import Helper

class HelperTestCase(unittest.TestCase):
    """tests for helper"""

    def test_fetch_examples(self):
        data = Helper().fetch_examples()
        self.assertEqual(type(data), list)
        print("passed ")

    def test_make_prompt(self):
        query = Helper().make_prompt()
        self.assertEqual(type(query), str)
        print("passed")


if __name__ == '__main__':
    unittest.main()
