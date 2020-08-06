class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# recursive:
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse(head, None)

    def reverse(self, head, reverse_h):
        if not head:
            return reverse_h
        tmp = head.next
        head.next = reverse_h
        return self.reverse(tmp, head)


# iterative:
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = None
        while head:
            tmp = head.next
            head.next = node
            node = head
            head = tmp
        return node
