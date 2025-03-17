package main

// import "fmt"

// a better way to do this could be to keep an array of ints, but this works with all unicode characters

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	seen := map[byte]int{}

	// collect all the characters from s
	for i := 0; i <= len(s)-1; i++ {
		if _, ok := seen[s[i]]; ok {
			seen[s[i]]++
		} else {
			seen[s[i]] = 1
		}
	}

	// check all the characters from j
	for i := 0; i <= len(s)-1; i++ {
		// iterate and delete when zero
		if v, ok := seen[t[i]]; ok {
			if v == 1 {
				delete(seen, t[i])
			} else {
				seen[t[i]]--
			}
		} else {
			return false
		}
	}
	if len(seen) > 0 {
		return false
	}
	return true
}

// func main() {
// 	s := "racecar"
// 	t := "bcrerac"
// 	fmt.Println(isAnagram(s, t))
// }
