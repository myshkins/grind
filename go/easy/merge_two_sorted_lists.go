package main


// Definition for singly-linked list.
type ListNode struct {
  Val int
  Next *ListNode
}

func less(a *ListNode, b *ListNode) (*ListNode, *ListNode) {
  switch {
  case a == nil && b == nil:
    return nil, nil
  case a == nil && b != nil:
    return b, nil
  case a != nil && b == nil:
    return a, nil
  }

  if a.Val <= b.Val {
    return a, b
  } else {
    return b, a
  }
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
  i, j := less(list1, list2)
  if i == nil {
    return i
  }
  if i.Next == nil {
    i.Next = j
    if j == nil {
      j = nil
    } else {
      j = j.Next
    }
  } else {
    i.Next, j = less(i.Next, j)
  }
  head := i

  for {
    if i == nil {
      i.Next = j
      if j == nil {
        j = nil
      } else {
        j = j.Next
      }
    } else {
      i, j = less(i.Next, j)
      i.Next, j = less(i.Next, j)
    }
    if i == nil && j == nil {
      break
    }
  }
  
  return head
}
