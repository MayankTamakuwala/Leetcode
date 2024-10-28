# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Solution 1

        # n = 0
        # stack=[]
        # curr = root

        # while curr or stack:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
        #     curr = stack.pop()
        #     n+=1
        #     if n == k:
        #         return curr.val
        #     curr = curr.right

        # Solution 2

        vals = []
        def inorder_traversal(node):
            if node.left:
                inorder_traversal(node.left)

            vals.append(node.val)

            if node.right:
                inorder_traversal(node.right)

        inorder_traversal(root)
        return vals[k - 1]
