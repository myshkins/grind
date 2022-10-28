# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.head = None
        
    def insert(self, new):
        if not self.head:
            self.head = ListNode(new.val)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = ListNode(new.val)
        
    def mergeTwoLists(self, list1: list, list2: list) -> list:
        item1, item2 = list1, list2
        while item1 or item2:
            if not item1:
                self.insert(item2)
                item2 = item2.next
            elif not item2:
                self.insert(item1)
                item1 = item1.next
            elif item1.val >= item2.val:
                self.insert(item2)
                item2 = item2.next
            else:
                self.insert(item1)
                item1 = item1.next
        return self.head

class LinkedList:
    def __init__(self, input):
        self.head = None
        self.input = input

    def insert(self, new):
        node = self.head
        while node.next:
            node = node.next
        node.next = ListNode(val=new)

    def build_list(self):
        self.head = ListNode(val=self.input[0])
        for item in self.input[1:]:
            self.insert(item)


list1 = [1,2,4]
list2 = [1,3,4]

linklist1 = LinkedList(list1)
linklist1.build_list()

linklist2 = LinkedList(list2)
linklist2.build_list()

sol = Solution()
sol.mergeTwoLists(linklist1.head, linklist2.head)
print(sol.head)