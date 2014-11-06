# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def solve(n):

	def isDivisibleBy3or5(i): 
		return (x % 3 == 0) or (x % 5 == 0)

	multiplesOf3and5 = [x for x in range(n) if isDivisibleBy3or5(x)]

   	return sum(multiplesOf3and5)