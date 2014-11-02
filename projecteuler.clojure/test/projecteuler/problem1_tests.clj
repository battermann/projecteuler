(ns projecteuler.problem1-tests
  (:require [clojure.test :refer :all]
            [projecteuler.problem1 :refer :all]))

(deftest problem1-tests
  (testing "project euler problem 1"
  	(is (= (solve 0) 0))
  	(is (= (solve 3) 0))
  	(is (= (solve 4) 3))
    (is (= (solve 10) 23))
    (is (= (solve 1000) 233168))))
