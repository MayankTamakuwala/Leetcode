# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {val : i for i, val in enumerate(inorder)}

        def helper(left, right):
            if left > right:
                return None
            root = TreeNode(preorder[0])
            val = preorder.pop(0)
            inorder_idx = inorderMap[val]
            root.left = helper(left, inorder_idx - 1)
            root.right = helper(inorder_idx + 1, right)
            return root
        return helper(0, len(inorder) - 1)
