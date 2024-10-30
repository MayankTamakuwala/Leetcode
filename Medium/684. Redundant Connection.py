class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        connections = defaultdict(set)

        for i in range(1, len(edges) + 1):
            connections[i].add(i)

        for x, y in edges:
            if y in connections[x] or x in connections[y]:
                return [x,y]

            connections[x] = connections[x].union(connections[y])
            for c in connections[x]:
                connections[c] = connections[x]
