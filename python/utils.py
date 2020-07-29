class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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

