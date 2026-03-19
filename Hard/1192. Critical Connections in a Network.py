# 1192. Critical Connections in a Network
# There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

# A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

# Return all critical connections in the network in any order.


# Example 1:


# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.
# Example 2:

# Input: n = 2, connections = [[0,1]]
# Output: [[0,1]]

# Constraints:

# 2 <= n <= 105
# n - 1 <= connections.length <= 105
# 0 <= ai, bi <= n - 1
# ai != bi
# There are no repeated connections.

from collections import defaultdict
from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj_list = defaultdict(list)
        for a, b in connections:
            adj_list[a].append(b)
            adj_list[b].append(a)

        disc = [-1]*n
        low = [-1]*n
        time = 0
        res = []

        def dfs(par, node):
            nonlocal time

            disc[node] = time
            low[node] = time
            time += 1

            for neigh in adj_list[node]:
                if neigh == par:
                    continue
                elif disc[neigh] != -1:
                    low[node] = min(disc[neigh], low[node])
                else:
                    dfs(node, neigh)
                    low[node] = min(low[node], low[neigh])
                    if low[neigh] > disc[node]:
                        res.append([neigh, node])

        dfs(-1, 0)

        return res

s = Solution()

print(s.criticalConnections(6, [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]]))
