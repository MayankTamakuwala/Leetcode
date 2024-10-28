# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, leftLimit, rightLimit):
            if not node:
                return True

            if not (node.val<rightLimit and node.val>leftLimit):
                return False

            l = validate(node.left, leftLimit, node.val)
            if not l:
                return False
            r = validate(node.right, node.val, rightLimit)

            return l and r

        return validate(root, float("-inf"), float('inf'))
