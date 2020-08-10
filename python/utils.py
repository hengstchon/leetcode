class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

    def __bool__(self):
        return bool(self.val)


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


def tree_to_arr(root):
    arr = [root.val]
    stack = [root]
    while stack:
        node = stack.pop(0)
        if node.left:
            arr.append(node.left.val)
            stack.append(node.left)
        if not node.left and node.right:
            arr.append(None)
        if node.right:
            arr.append(node.right.val)
            stack.append(node.right)
    return arr

