# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def ggt(a, b):
  rest = a%b
  while rest != 0:
    a = b
    b = rest
    rest = a%b
  return b

def kgv(a, b):
  return abs(a*b)/ggt(a,b)

def solve(n):
  return reduce(lambda x,y: kgv(x,y), range(1, n+1))
