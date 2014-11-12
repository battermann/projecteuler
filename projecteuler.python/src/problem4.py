# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
  s = str(n)
  for i in range(len(s) // 2):
    if s[i] != s[len(s)-1-i]: return False
  return True

def solve(n):
  min = 10**(n-1)
  max = 10**(n)-1
  reversed_n_digit_numbers = range(max, min-1, -1)
  largest_palindrome = 0
  for palindrome in [x*y for x in reversed_n_digit_numbers for y in reversed_n_digit_numbers if is_palindrome(x*y)]:
    if palindrome > largest_palindrome: largest_palindrome = palindrome
  return largest_palindrome
