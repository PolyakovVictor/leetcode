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
q = create_tree([1, 2, 1])


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return True


obj = Solution()
print(obj.isSameTree(p, q))
