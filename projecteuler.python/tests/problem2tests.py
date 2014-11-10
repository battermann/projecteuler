import unittest, sys
sys.path.append('..\src')
import problem2

class Problem2Tests(unittest.TestCase):

    def test_solve_below50_shouldEqual_44(self):
        self.assertEqual(problem2.solve(50), 44)

    def test_solve_below4000000_shouldEqual_4613732(self):
        self.assertEqual(problem2.solve(4000000), 4613732)

if __name__ == '__main__':
    unittest.main()