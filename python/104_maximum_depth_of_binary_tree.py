from utils import TreeNode, arr_to_tree
import unittest
from collections import deque

null = None

# BFS + deque
class Solution1:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        # 1: level
        queue = deque([(root, 1)])
        while queue:
            node, val = queue.popleft()
            if node.left:
                queue.append((node.left, val + 1))
            if node.right:
                queue.append((node.right, val + 1))

        return val


# Recursive
class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return max(l, r) + 1


class Test(unittest.TestCase):
    def test(self):
        s = Solution2()
        data = [([3, 9, 20, null, null, 15, 7], 3)]

        for d in data:
            tree = arr_to_tree(d[0])
            self.assertEqual(s.maxDepth(tree), d[1])


if __name__ == "__main__":
    unittest.main()
