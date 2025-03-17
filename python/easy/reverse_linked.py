# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev

# def reverseList(head):
#     def switch_next(link, prev):
#         if link.next is None:
#             return link
#         result = switch_next(link.next, link)
#         link.next = prev
#         return result
#     return switch_next(head, None)

five = ListNode(5, None)
four = ListNode(4, five)
three = ListNode(3, four)
two = ListNode(2, three)
head = ListNode(1, two)

print(reverseList(head))
