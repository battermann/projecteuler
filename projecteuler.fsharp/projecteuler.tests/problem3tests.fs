module problem3tests

open problem3
open NUnit.Framework
open FsUnit

[<TestCase(2,2)>]
[<TestCase(3,3)>]
[<TestCase(4, 2)>]
[<TestCase(21,7)>]
[<TestCase(23,23)>]
[<TestCase(13195,29)>]
let ``largest prime factor should equal`` ((n:int), (expected:int)) = 
    solve (n |> int64) |> should equal (expected |> int64)

[<Test>]
let ``largest prime factor of 600851475143 should equal 6857`` ()
    = solve 600851475143L |> should equal 6857L

