# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# method 1:
# hashmap
# time complexity: O(m+n)
# space complexity: O(m) or O(n)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        s = set()
        while headA:
            s.add(headA)
            headA = headA.next
        while headB:
            if headB in s:
                return headB
            headB = headB.next


# method 2:
# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB
        while pA is not pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        # pA is pB only happens in two situations:
        # 1. pA and pB reach the intersection node
        # 2. pA and pB reand the end (None)
        return pA
