class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # Solution 1

        if len(edges) != n - 1:
            return False

        adjList = defaultdict(list)

        for x, y in edges:
            adjList[x].append(y)
            adjList[y].append(x)

        queue = [0]
        visited = set()
        while queue:
            node = queue.pop(0)

            if node in visited:
                continue

            visited.add(node)
            for neigbr in adjList[node]:
                queue.append(neigbr)

        return len(visited) == n

        # Solution 2

        # connections = defaultdict(set)

        # for i in range(n):
        #     connections[i].add(i)

        # for x, y in edges:
        #     if x in connections[y] or y in connections[x]:
        #         return False

        #     connections[x] = connections[x].union(connections[y])

        #     for c in connections[x]:
        #         connections[c] = connections[x]

        # return True
