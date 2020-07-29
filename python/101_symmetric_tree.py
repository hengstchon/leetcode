# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive
class Solution1:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isSym(root.left, root.right)

    def isSym(self, t1, t2):
        if t1 and t2:
            return (
                t1.val == t2.val
                and self.isSym(t1.left, t2.right)
                and self.isSym(t1.right, t2.left)
            )
        return t1 == t2


# Iterative
# 在 while 循环中，分 4 种情况：
# 1. t1，t2 都为空，进行下一轮判断
# 2. t1，t2 仅有一个为空，return Fasle
# 3. t1，t2 都不为空，但 val 不相等，return False
# 4. t1，t2 都不为空，且 val 相等，压他们的子节点进 queue，进行下一轮判断
class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = [(root.left, root.right)]
        while queue:
            t1, t2 = queue.pop(0)
            print("t1 , t2")
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            print("t1, t2: ", t1.val, t2.val)
            if t1.val != t2.val:
                return False
            queue += [(t1.left, t2.right), (t1.right, t2.left)]


import unittest


def arr_to_tree(arr):
    if not arr:
        return
    root = TreeNode(arr[0])
    nodes = [root]
    for i in range(1, len(arr), 2):
        node = nodes.pop(0)
        node.left = TreeNode(arr[i])
        node.right = TreeNode(arr[i + 1])
        nodes += [node.left, node.right]
    return root


class Test(unittest.TestCase):
    global null
    null = None

    def test(self):
        s = Solution2()
        data = [
            ([1, 2, 2, 3, 4, 4, 3], True),
            ([1, 2, 2, null, 3, null, 3], False),
            ([1, 2, 2, 3, null, null, 3], True),
            ([9, -42, -42, null, 76, 76, null, null, 13, null, 13], False),
            ([], True),
        ]

        for d in data:
            t = arr_to_tree(d[0])
            self.assertEqual(s.isSymmetric(t), d[1])


if __name__ == "__main__":
    unittest.main()
