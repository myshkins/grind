package main

import (
  "fmt"
  "regexp"
  "strings"
)

func isPalindrome(s string) bool {
  re := regexp.MustCompile(`[^a-zA-Z0-9]`)
  ns := re.ReplaceAllString(s, "")
  ns = strings.ToLower(ns)
  for i, j := 0, len(ns)-1; i <= len(ns)/2; i, j = i+1, j-1 {
    if ns[i] != ns[j] {
      return false
    }
  }
  return true
}

// func main() {
//   s := "A man, a plan, a canal: Panama"
//   fmt.Println(isPalindrome(s))
// }
