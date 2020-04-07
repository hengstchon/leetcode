# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# method 1
# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        while curr:
            while curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
            curr = curr.next
        return head


# method 2
# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
