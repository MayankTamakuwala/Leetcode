# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def dsf(n1, n2, newTree):
            if not n1 and not n2:
                return None

            v1 = n1.val if n1 else 0
            v2 = n2.val if n2 else 0

            t = v1 + v2
            newTree = TreeNode(t)

            newTree.left = dsf(
                n1.left if n1 and n1.left else None,
                n2.left if n2 and n2.left else None,
                newTree.left
            )

            newTree.right = dsf(
                n1.right if n1 and n1.right else None,
                n2.right if n2 and n2.right else None,
                newTree.right
            )

            return newTree

        return dsf(root1, root2, None)
