package main

import "fmt"

func search(nums []int, target int) int {
  low, hi := 0, len(nums)-1
  if nums[0] == target {
    return 0
  }

  for low <= hi {
    mid := low + (hi - low)/2
    if target < nums[mid] {
      hi = mid - 1
    } else if target > nums[mid] {
      low = mid + 1
    } else {
      return mid
    }
  }
  return -1
}

func main() {
  nums := []int{2, 5}
  fmt.Println(search(nums, 5))
}
