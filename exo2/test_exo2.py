#tests

import unittest
from exo2 import solution

class TestSolutionFunction(unittest.TestCase):

    def test_true_cases(self):
        fixed_tests_True = [
            ("samurai", "ai"),
            ("ninja", "ja"),
            ("sensei", "i"),
            ("abc", "abc"),
            ("abcabc", "bc"),
            ("fails", "ails"),
        ]

        for test_case in fixed_tests_True:
            with self.subTest(test_case=test_case):
                self.assertTrue(solution(*test_case))

    def test_false_cases(self):
        fixed_tests_False = [
            ("sumo", "omo"),
            ("samurai", "ra"),
            ("abc", "abcd"),
            ("ails", "fails"),
            ("this", "fails"),
            ("spam", "eggs"),
        ]

        for test_case in fixed_tests_False:
            with self.subTest(test_case=test_case):
                self.assertFalse(solution(*test_case))

if __name__ == '__main__':
    unittest.main()
