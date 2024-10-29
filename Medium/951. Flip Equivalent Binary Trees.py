# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def isSymmetric(l, r):
            if not l and not r:
                return True

            if not l or not r:
                return False

            if l.val != r.val:
                return False

            rec1 = isSymmetric(l.left, r.left) and isSymmetric(l.right, r.right)
            if rec1:
                return True
            rec2 = isSymmetric(l.left, r.right) and isSymmetric(l.right, r.left)

            return rec1 or rec2

        return isSymmetric(root1, root2)
