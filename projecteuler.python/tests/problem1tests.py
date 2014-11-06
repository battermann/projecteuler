import unittest, sys
sys.path.append('..\src')
import problem1

class Problem1Tests(unittest.TestCase):

    def test_solve_below10_shouldEqual_23(self):
        self.assertEqual(problem1.solve(10), 23)

    def test_solve_below1000_shouldEqual_233168(self):
        self.assertEqual(problem1.solve(1000), 233168)

if __name__ == '__main__':
    unittest.main()