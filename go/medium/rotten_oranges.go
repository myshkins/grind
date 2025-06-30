package main

// import "fmt"

// this is the naive approach. BFS is the efficient solution. It's multi source
// bfs. use each rotten orange as a starting point to add to the queue

// check if edge, return valid neighbor cooordinates
func whichNeighbors(width, height, x, y int) [][2]int {
  var locations [][2]int
  if y != 0 {
    locations = append(locations, [2]int{x, y-1})
  }
  if y != height - 1 {
    locations = append(locations, [2]int{x, y+1})
  }
  if x != 0 {
    locations = append(locations, [2]int{x-1, y})
  }
  if x != width - 1 {
    locations = append(locations, [2]int{x+1, y})
  }
  return locations
}

func orangesRotting(grid [][]int) int {
  // iterate until all 2s in the grid or no change from previous iteration    
  // for each iteration, examine all the squares and keep a map of all the
  // squares that become rotten. after processing, make rotten

  // one iteration to spread rottenness
  minutes := 0
  lastFresh := 0
  for {
    fresh := 0
    toRot := make(map[[2]int]struct{})
    for y, row := range grid {
      for x, val := range row {
        if val == 1 {
          fresh ++
          continue
        }
        if val != 2 {
          continue
        }
        // check if edge location
        neighbLocations := whichNeighbors(len(grid[0]), len(grid), x, y)
        // mark neighbors in toRot
        for _, loc := range neighbLocations {
          if grid[loc[1]][loc[0]] == 2 || grid[loc[1]][loc[0]] == 0 {
            continue
          }
          toRot[loc] = struct{}{}
        }
      } 
    }

    // check if no change since last iteration, if so, not possible
    if fresh != 0 && fresh == lastFresh {
      return - 1
    }
    lastFresh = fresh

    if fresh == 0 {
      return minutes
    }

    for k, _ := range toRot {
      row := k[1]
      col := k[0]
      if grid[row][col] == 1 {
        fresh --
        grid[row][col] = 2
      }
    }
    minutes ++

    if fresh == 0 {
      return minutes
    }
 }
}

// func main() {
//   grid := [][]int{{0,2}}
//   res := orangesRotting(grid)  
//   fmt.Println(res)
// }
