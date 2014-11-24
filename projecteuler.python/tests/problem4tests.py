import unittest, sys
sys.path.append('../src')
import problem4

class Problem4Tests(unittest.TestCase):

  def test_is_palindrome(self):
    self.assertEqual(problem4.is_palindrome(1), True)
    self.assertEqual(problem4.is_palindrome(11), True)
    self.assertEqual(problem4.is_palindrome(99), True)
    self.assertEqual(problem4.is_palindrome(121), True)
    self.assertEqual(problem4.is_palindrome(989), True)
    self.assertEqual(problem4.is_palindrome(2332), True)
    self.assertEqual(problem4.is_palindrome(9009), True)
    self.assertEqual(problem4.is_palindrome(1235321), True)
    self.assertEqual(problem4.is_palindrome(12355555321), True)

    self.assertEqual(problem4.is_palindrome(12), False)
    self.assertEqual(problem4.is_palindrome(321), False)
    self.assertEqual(problem4.is_palindrome(1561), False)
    self.assertEqual(problem4.is_palindrome(1234565432), False)

  def test_largest_palindrome_2_digits(self):
    self.assertEqual(problem4.solve(2), 9009)

  def test_largest_palindrome_3_digits(self):
    self.assertEqual(problem4.solve(3), 906609)

if __name__ == '__main__':
    unittest.main()
