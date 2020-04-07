"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


# method 1:
# use dict(hashmap)
# time complexity: O(n)
# space complexity: O(n)

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return

        d = {}
        m = n = head

        # construct mappings
        while m:
            d[m] = Node(m.val)
            m = m.next

        # connect copied items to linked list
        while n:
            d[n].next = d.get(n.next)
            d[n].random = d.get(n.random)
            n = n.next

        return d[head]


# method 2:
# add a copied node after each original node
# time complexity: O(n)
# space complexity: O(1)

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return

        m = n = head

        # interweave old nodes and copied nodes
        # like: A -> A' -> B -> B' -> C -> C'...
        while m:
            node = Node(m.val)
            node.next = m.next
            m.next = node
            m = m.next.next

        # if n has random pointer
        # link that random pointer's next node
        # to the random pointer of n's copied node
        while n:
            if n.random:
                n.next.random = n.random.next
            n = n.next.next

        # separate original list and copied list
        newhead = head.next
        pold = head
        pnew = newhead
        while pnew.next:
            pold.next = pold.next.next
            pold = pold.next
            pnew.next = pnew.next.next
            pnew = pnew.next

        return newhead
