# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev, minDiff = None, float('inf')

        def inorder(node):
            nonlocal prev, minDiff

            if node.left:
                inorder(node.left)

            if prev is not None:
                minDiff = min(minDiff, abs(node.val - prev.val))
            prev = node

            if node.right:
                inorder(node.right)

        inorder(root)
        return minDiff
