(ns projecteuler.problem2-tests
  (:require [clojure.test :refer :all]
            [projecteuler.problem2 :refer :all]))

(deftest problem2-tests
  (testing "project euler problem 2"
  	(is (= (solve 50 ) 44))
  	(is (= (solve 4000000 ) 4613732))))
