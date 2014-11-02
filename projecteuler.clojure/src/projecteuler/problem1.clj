(ns projecteuler.problem1)

;If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
;The sum of these multiples is 23.
;Find the sum of all the multiples of 3 or 5 below 1000.

(defn solve [n] 
	(defn is-divisible-by-3-or-5 [x] 
		(or (= (rem x 3) 0) (= (rem x 5) 0)))
	(reduce + (filter is-divisible-by-3-or-5 (range 1 n))))
