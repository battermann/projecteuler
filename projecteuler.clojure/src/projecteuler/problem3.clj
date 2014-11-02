(ns projecteuler.problem3)

;The prime factors of 13195 are 5, 7, 13 and 29.
;What is the largest prime factor of the number 600851475143 ?

(defn solve 
	([n] (solve n n 2 2))
	([number limit current largest-prime]
	   (if (> current limit)
	   		largest-prime
	   		(if (= (mod number current) 0)
	   			(solve (/ number current) limit current current)
	   			(solve number limit (inc current) largest-prime)))))


