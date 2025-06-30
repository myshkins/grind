package main

import (
  "fmt"
  "math"
)

func buildMap() map[int]int {
  s := "0123456789"
  m := make(map[int]int)
  for i, c := range s {
    m[int(c)] = i
  }
  return m
}

func myAtoi(s string) int {
  fmt.Println(s)

  m := buildMap()
  fmt.Println(m)

  // collect the digits
  var digits []int
  for _, r := range s {
    if _, ok := m[int(r)]; !ok {
      break
    }
    digits = append(digits, m[int(r)])
  }
  fmt.Printf("digits: %v\n", digits)

  // process the digits into an integer
  number := 0
  for i, j := 0, len(digits); j > 0; i++ {
    j--
    decimalMultiplier := int(math.Pow(float64(10), float64(j)))
    number += (decimalMultiplier * digits[i])
  }

  return number
}

// func main() {
//   result := myAtoi("432")
//   fmt.Println(result)
// }
