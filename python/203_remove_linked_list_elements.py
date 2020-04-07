# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        curr = dummy = ListNode(-1)
        dummy.next = head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next
