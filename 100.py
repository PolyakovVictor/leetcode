from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree(values):
    if not values:
        return None

    # Create the root node
    root = TreeNode(values[0])
    queue = [root]
    i = 1

    # Use a queue to construct the tree level by level
    while i < len(values):
        current = queue.pop(0)

        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root


# Create trees with the given values
p = create_tree([1, 2])
q = create_tree([1, null, 2])


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p.left.val or not q.left.val or not p.right.val or not q.right.val:
            return True
        if p.left.val != q.left.val or p.right.val != q.right.val:
            print(p.left.val, q.left.val, p.right.val, q.right.val)
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


obj = Solution()
print(obj.isSameTree(p, q))
