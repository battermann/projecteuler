module projecteuler.problem2tests

open projecteuler.problem2
open NUnit.Framework
open FsUnit

[<Test>]
let ``limit of 50 should equal 44`` ()
    = solve 50 |> should equal 44

[<Test>]
let ``limit of 4000000 should equal `` ()
    = solve 4000000 |> should equal 4613732


