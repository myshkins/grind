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
  /*
  find head, between a and b
  save head
  find head.next, between a.next and b, repoint (if needed)
  move to next, now head
  find next, repoint if necessary
  */
  a, b := less(list1, list2)
  head := a

  for b != nil {
    switch
    if a.Next == nil {
      a.Next = b // reassign next value
      a = b // move to next node for next iteration
      b = b.Next
    } else {
      a.Next, b = less(a.Next, b) // reassign next value
      a = a.Next // nove to next node for next iteration
    }
    }
  return head
}

func main() {
  a2 := ListNode{3, nil}
  a1 := ListNode{-9, &a2}
  b2 := ListNode{7, nil}
  b1 := ListNode{5, &b2}
  mergeTwoLists(&a1, &b1)
}

