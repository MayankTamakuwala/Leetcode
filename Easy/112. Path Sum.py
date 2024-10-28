# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node, sumVal):
            if not node:
                return False

            sumVal += node.val

            if not node.left and not node.right:
                if sumVal == targetSum:
                    return True
                return False

            l_dfs = dfs(node.left, sumVal)

            if l_dfs:
                return True

            r_dfs = dfs(node.right, sumVal)
            
            return l_dfs or r_dfs

        return dfs(root, 0)
