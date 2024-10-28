# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0

            l = dfs(node.left)

            if l == -1:
                return -1

            r = dfs(node.right)
            
            if r == -1 or l == -1 or abs(l - r) > 1:
                return -1
            
            return 1 + max(l,r)

        h = dfs(root)
        return not h == -1
