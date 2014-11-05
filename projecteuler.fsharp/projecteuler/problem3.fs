module problem3

// The prime factors of 13195 are 5, 7, 13 and 29.
// What is the largest prime factor of the number 600851475143 ?

let solve n =
    let fastinc i = 
        match i with
        | i when i % 2L = 0L -> i + 1L
        | _ -> i + 2L

    let rec solve candidate divisor =
        match divisor with
        | d when d > (candidate / 2L) -> candidate
        | d when candidate % d = 0L -> solve (candidate / divisor) 2L
        | _ -> solve candidate (fastinc divisor)

    solve n 2L