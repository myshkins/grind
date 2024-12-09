package main

// import "fmt"

func twoSum(nums []int, target int) []int {
  result := make([]int, 0)
  seen := make(map[int]int)
  for i, v := range nums {
    complement := target - v
    comp_indx, ok := seen[complement]
    if ok {
      result = append(result, i, comp_indx)
      return result
    } 
    _, ok = seen[v]
    if ! ok {
      seen[v] = i
    }
  }
  result = append(result, 9,9)
  return result
}

// func main() {
//   nums := []int{3,2,4}
//   target := 6
//   answer := twoSum(nums, target)
//   fmt.Println(answer)
// }
