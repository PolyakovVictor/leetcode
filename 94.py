from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(root: Optional[TreeNode], result: List):
            if not root:
                return []
            preorder(root=root.left, result=result)
            result.append(root.val)
            preorder(root=root.right, result=result)

        result = []
        preorder(root=root, result=result)
        return result


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

obj = Solution()
print(obj.inorderTraversal(root=root))
