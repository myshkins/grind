package main

import (
  "fmt"
)

func printSubstring(sub map[string]struct{}) {
  for k, _ := range sub {
    fmt.Println(k)
  }
}

func lengthOfLongestSubstring(s string) int {
  i := 0
  j := 0
  sub := make(map[string]struct{})  // letter: {}
  result := 0
  sofar := 0
  for j <= (len(s) - 1) {
    printSubstring(sub)
    letter := string(s[j])
    fmt.Println(letter)
    if _, ok := sub[letter]; !ok {
      fmt.Println("new")
      sub[letter] = struct{}{}
      j++
      sofar ++
      if sofar > result {
        result = sofar
      }
      fmt.Printf("\nj=%d\n", j)
    } else {
      fmt.Println("repeat")
      // advance i until s[i-1] == s[j] 
      fmt.Printf("\ni=%d\n", i)
      for s[i] != s[j] {
        fmt.Printf("\nj=%d\n", j)
        i++
        delete(sub, string(s[i-1]))
      }
      i++
      delete(sub, string(s[i-1]))
      sofar = j - i
    }

  }
  return result
}

// func main() {
//   s := "pwwkew"
//   res := lengthOfLongestSubstring(s)
//   fmt.Printf("\nres = %v\n", res)
// }
