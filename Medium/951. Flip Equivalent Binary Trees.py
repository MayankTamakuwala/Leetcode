# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        l = root1
        r = root2

        if not l and not r:
            return True

        if not l or not r:
            return False

        if l.val != r.val:
            return False

        rec1 = self.flipEquiv(l.left, r.left) and self.flipEquiv(l.right, r.right)
        if rec1:
            return True
        rec2 = self.flipEquiv(l.left, r.right) and self.flipEquiv(l.right, r.left)

        return rec1 or rec2
