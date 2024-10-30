class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        routeMap = defaultdict(set)
        edges = set(map(tuple, connections))

        for s, t in connections:
            routeMap[s].add(t)
            routeMap[t].add(s)

        visited = set()
        res = 0

        def dfs(target):
            nonlocal res
            for neigbr in routeMap[target]:
                if neigbr in visited:
                    continue
                if (neigbr, target) not in edges:
                    res += 1
                visited.add(neigbr)
                dfs(neigbr)

        visited.add(0)
        dfs(0)

        return res
