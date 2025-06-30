package main

import (
  "fmt"
)

type Node struct {
    Val int
    Neighbors []*Node
}

// func dfs(adj map[int][]int, node *Node) {
//   if _, ok := adj[node.Val]; ok {
//     return
//   } else {
//     adj[node.Val] = []int{}
//     for _, n := range node.Neighbors {
//       adj[node.Val] = append(adj[node.Val], n.Val)
//       dfs(adj, n)
//     }
//   }
// }

// func cloneGraph(node *Node) *Node {
//   adj := make(map[int][]int)
//   dfs(adj, node)
//   // initialize each copy node
//   copies := []*Node{}
//   for i := 1; i <= len(adj) ; i++ {
//     copies = append(copies, &Node{Val: i})
//   }
//   // add neighbors to each copy
//   // i is index in copies slice and index in adj
//   for i, c := range copies {
//     for _, val := range adj[i+1] {
//       c.Neighbors = append(c.Neighbors, copies[val-1])
//     }
//   }
//   return copies[0]
// }

func printQueue(queue []*Node) {
  fmt.Println("queue")
  for _, n := range queue {
    fmt.Printf("%4d\n", n.Val)
  }
}

func bfs(adj map[int][]int, node *Node) {
  queue := []*Node{node}  //each int represents a node by its value
  seen := make(map[int]struct{})
  seen[node.Val] = struct{}{}

  for len(queue) > 0 {
    current := queue[len(queue) - 1]
    queue = queue[:len(queue) - 1]

    // mark as seen, add neighbs
    for _, n := range current.Neighbors {
      adj[current.Val] = append(adj[current.Val], n.Val)
      if _, ok := seen[n.Val]; !ok {
        seen[n.Val] = struct{}{}
        queue = append(queue, n)
      }
    }
  }
  fmt.Println(adj)
}

func cloneGraph(node *Node) *Node {
  adj := make(map[int][]int)
  bfs(adj, node)
  // initialize each copy node
  copies := []*Node{}
  for i := 1; i <= len(adj) ; i++ {
    copies = append(copies, &Node{Val: i})
  }
  // add neighbors to each copy
  // i is index in copies slice and index in adj
  for i, c := range copies {
    for _, val := range adj[i+1] {
      c.Neighbors = append(c.Neighbors, copies[val-1])
    }
  }
  return copies[0]
}

// func main() {
//   var one = Node{Val: 1, Neighbors: []*Node{}}
//   var two = Node{Val: 2, Neighbors: []*Node{}}
//   var three = Node{Val: 3, Neighbors: []*Node{}}
//   var four = Node{Val: 4, Neighbors: []*Node{}}
//   one.Neighbors = []*Node{&two, &four}
//   two.Neighbors = []*Node{&one, &three}
//   three.Neighbors = []*Node{&two, &four}
//   four.Neighbors = []*Node{&three, &one}
//  
//   copyRoot := cloneGraph(&one)
//   newAdj := make(map[int][]int)
//   bfs(newAdj, copyRoot)
// }
