# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        node = head
        seen = []
        while node:
            seen.append(node)
            node = node.next
        return seen[(len(seen) // 2)]