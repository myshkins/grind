# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def hasCycle(self, head) -> bool:
#         checked = {}
#         link = head
#         while link:
#             if checked.get(link.next) is link:
#                 return True
#             checked[link.val] = link
#             link = link.next
#         return False

class Solution:
    def hasCycle(self, head) -> bool:
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next.next
        while fast and fast.next:
            if slow is fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

