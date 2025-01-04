package main

var initColor int
var targetColor int
var gImage [][]int

func scanAndChange(row, col int) {
  gImage[row][col] = targetColor

  adjacents := [][]int{
    {row+1, col},
    {row, col+1},
    {row-1, col},
    {row, col-1},
  }

  for _, cell := range adjacents {
    // check that the cell is not outside image boundary
    if cell[0] > len(gImage)-1 || cell[0] < 0 {
      continue
    }
    if cell[1] > len(cell)-1 || cell[1] < 0 {
      continue
    }
    
    //check if the cell isn't already the right color, or been visited already
    if cellValue := gImage[cell[0]][cell[1]]; cellValue != targetColor && cellValue == initColor {
      scanAndChange(cell[0], cell[1])
    }
  }
}


func floodFill(image [][]int, sr int, sc int, color int) [][]int {
  /*
  recursively
  change color
  find adjacents
  if ok on one of adjacents
    recurse
  return if no adjacent matches
  */

  initColor = image[sr][sc]
  targetColor = color
  gImage = image
  
  scanAndChange(sr, sc)
  return image
}
