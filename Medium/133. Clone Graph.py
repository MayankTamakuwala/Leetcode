"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        newNodes = {}

        def dfs(node):
            if node in newNodes:
                return newNodes[node]

            copyNode = Node(node.val)
            newNodes[node] = copyNode

            for n in node.neighbors:
                copyNode.neighbors.append(dfs(n))

            return copyNode

        return dfs(node)
