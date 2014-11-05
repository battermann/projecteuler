(ns projecteuler.problem3)

;The prime factors of 13195 are 5, 7, 13 and 29.
;What is the largest prime factor of the candidate 600851475143 ?

(defn solve [n]
	(defn is-divisible-by [x y] (if (= (rem x y) 0) true false))
	(defn fast-inc [i] (if (is-divisible-by i 2) (inc i) (+ i 2)))
	
	(loop [candidate n
		   divisor 2]
		(if (> divisor (/ candidate 2))
			candidate
			(if (is-divisible-by candidate divisor)
				(recur (/ candidate divisor) 2)
				(recur candidate (fast-inc divisor))))))