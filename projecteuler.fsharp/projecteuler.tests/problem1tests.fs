module problem1tests

open problem1
open NUnit.Framework
open FsUnit

[<Test>]
let ``below 10 should equal 23`` ()
    = solve 10 |> should equal 23

[<Test>]
let ``below 1000 should equal 233168`` ()
    = solve 1000 |> should equal 233168
