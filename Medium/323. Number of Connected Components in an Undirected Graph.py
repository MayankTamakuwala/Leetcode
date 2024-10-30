class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()

        adjList = defaultdict(list)

        for x, y in edges:
            adjList[x].append(y)
            adjList[y].append(x)

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for neigbr in adjList[node]:
                dfs(neigbr)

        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        return res
