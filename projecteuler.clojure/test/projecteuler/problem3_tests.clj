(ns projecteuler.problem3-tests
  (:require [clojure.test :refer :all]
            [projecteuler.problem3 :refer :all]))

(deftest problem3-time-function
  (testing "function execution time problem 3"
    (time (solve 600851475143))))

(deftest problem3-tests
	(testing "project euler problem 3"
  	(is (= (solve 2 ) 2))
  	(is (= (solve 3 ) 3))
  	(is (= (solve 4 ) 2))
  	(is (= (solve 21 ) 7))
  	(is (= (solve 23 ) 23))
  	(is (= (solve 13195) 29))))

(deftest problem3-tests2
  (testing "project euler problem 3"
    (is (= (solve 600851475143) 6857))))
