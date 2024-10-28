# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, sumVal):
            if not node:
                return 
            sumVal = sumVal*10 + node.val

            if not node.left and not node.right:
                return sumVal
            
            l_dfs = dfs(node.left, sumVal)
            r_dfs = dfs(node.right, sumVal)

            return l_dfs + r_dfs
        return dfs(root, 0)
