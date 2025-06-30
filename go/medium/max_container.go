package main

func lower(x1 int, x2 int) int {
  if x1 > x2 {
    return x2
  }
  return x1
}

func moveI(ih, jh int) bool {
  if ih > jh {
    return false
  }
  return true
}

func maxArea(height []int) int {
  // initialize two pointers
  i := 0
  j := len(height) - 1

  best := lower(height[i], height[j]) * (j - i)

  // iterate until both pointer reach the end
  for i <= j {
    volume := lower(height[i], height[j]) * (j - i)
    if volume > best {
      best = volume
    }
    if moveI(height[i], height[j]) {
      i++
    } else {
      j--
    }
  }

  return best
}

// func main() {
// }
