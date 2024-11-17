class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adjList = defaultdict(set)
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    adjList[i+1].add(j+1)
                    adjList[j+1].add(i+1)

        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for neig in adjList[node]:
                dfs(neig)
            return

        res = 0
        for i in range(1, n+1):
            if i not in visited:
                res += 1
                dfs(i)
        return res
