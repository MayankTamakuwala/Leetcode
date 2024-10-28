# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(l, r):

            if not l and not r:
                return True

            if not l or not r:
                return False

            if l.val != r.val:
                return False

            l_dfs = dfs(l.left,r.right)

            if not l_dfs:
                return False

            r_dfs = dfs(l.right,r.left)
            
            return l_dfs and r_dfs

        if not root.left and not root.right:
            return True

        if not root.left or not root.right:
            return False
        
        return dfs(root.left, root.right)