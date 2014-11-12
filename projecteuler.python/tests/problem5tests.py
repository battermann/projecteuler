import unittest, sys
sys.path.append('..\src')
import problem5

class Problem5Tests(unittest.TestCase):

  def test_kgv(self):
    self.assertEqual(problem5.kgv(2, 2), 2)
    self.assertEqual(problem5.kgv(10, 15), 30)

  def test_smallest_evenly_devisible(self):
    self.assertEqual(problem5.solve(10), 2520)

  def test_smallest_evenly_devisible(self):
    self.assertEqual(problem5.solve(20), 232792560)

if __name__ == '__main__':
    unittest.main()
