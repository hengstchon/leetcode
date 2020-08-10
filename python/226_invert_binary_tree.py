from utils import arr_to_tree, tree_to_arr
import unittest
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive:
class Solution1:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = (
                self.invertTree(root.right),
                self.invertTree(root.left),
            )
        return root


# BFS
class Solution2:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                node.left, node.right = node.right, node.left
                queue += [node.left, node.right]
        return root


# DFS
class Solution3:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = [root]
        while stack:
            # diff with BFS
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += [node.left, node.right]
                print(stack)
        return root


class Test(unittest.TestCase):
    def test(self):
        s = Solution3()
        data = [
            ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
            (
                [4, 2, 7, 1, 3, 6, 9, 2, 3, 4, 5, 6, 7],
                [4, 7, 2, 9, 6, 3, 1, 7, 6, 5, 4, 3, 2],
            ),
        ]
        for d in data:
            self.assertEqual(tree_to_arr(s.invertTree(arr_to_tree(d[0]))), d[1])


if __name__ == "__main__":
    unittest.main()
