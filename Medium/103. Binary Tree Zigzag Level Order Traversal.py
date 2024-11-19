# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        leftToRight = True
        queue = [root]
        res = []

        while queue:
            queueLength = len(queue)
            collect = [0] * queueLength
            for i in range(queueLength):
                node = queue.pop(0)
                if leftToRight:
                    collect[i] = node.val
                else:
                    collect[queueLength - i - 1] = node.val

                if node.left:
                        queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            leftToRight = not leftToRight
            res.append(collect)

        return res
