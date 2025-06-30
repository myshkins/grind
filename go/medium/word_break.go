package main

import "fmt"
// FIX: this should be dfs, it's close but not quite.
// recursively search for words. Find all word matches starting from given index,
// for each match, call findWords to get next match, so match returns word list or nil
// return word list when last character checked and last word found
// return nil when no matches but still characters left to check
func findWords(s string, index int, wordMap map[string]struct{}) bool {
  var word []byte
  matches := make(map[string]int)
  outer:
  for i := index; i < len(s); i++ {
    word = append(word, s[i])
    _, ok := wordMap[string(word)]
    switch {
    case ok && i != len(s) -1: // find a match
      matches[string(word)] = i + 1
    case !ok && len(matches) > 0: // there is a previous match, and no match with current character
      break outer
    case ok && i == len(s) - 1: // last character and last match
      return true
    }
  }
  result := false
  for _, newIndex := range matches {
    result = findWords(s, newIndex, wordMap)
    if result {
      return result
    } 
  }
  return result
  
}

func wordBreak(s string, wordDict []string) bool {
  // first convert wordDict slice into a map for fast lookup time
  wordMap := make(map[string]struct{})
  for _, word := range wordDict {
    wordMap[word] = struct{}{}
  }

  // look for first word, iterate over characters, grow the character group
  // until a word match is found. continue searching in case of multiple matches
  // stop when no matches found.
  return findWords(s, 0, wordMap)
}

func main() {
  s := "leetcode"
  words := []string{"leet", "code"}
  res := wordBreak(s, words)
  fmt.Println(res)
}
