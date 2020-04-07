# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# method 1:
# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        d = set()
        while head:
            if head in d:
                return True
            else:
                d.add(head)
                head = head.next


# method 2:
# time complexity: O(n)
# space complexity: O(1)
# if there is a cycle, fast node will catch slow node
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False


# method 3
# similar with method 2
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
