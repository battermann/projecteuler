(ns projecteuler.problem3)

;The prime factors of 13195 are 5, 7, 13 and 29.
;What is the largest prime factor of the number 600851475143 ?

; Works with smaller numbers. Apparently not efficient enough.
(defn solve [n]
	(loop [number n
		     current (quot n 2)
		     largest n]
		(if (< current 2)
			largest
			(if (= (mod number current) 0) 
				(recur current (quot current 2) current) 
				(recur number (dec current) largest))))) 