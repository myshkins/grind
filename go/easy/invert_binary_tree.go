package main

// type TreeNode struct {
//     Val int
//     Left *TreeNode
//     Right *TreeNode
// }

func switchNodes(node *TreeNode) {
  if node.Left != nil {
    switchNodes(node.Left)
  }
  if node.Right != nil {
    switchNodes(node.Right)
  }
  node.Left, node.Right = node.Right, node.Left
  return
}

func invertTree(root *TreeNode) *TreeNode {
  /*
  recursively visit each node
    go to the left and right children if exist
  switch the left and right
  */
  if root == nil {
    return root
  }
  switchNodes(root)
  return root
}
