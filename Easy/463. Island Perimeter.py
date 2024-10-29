class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        res = 0

        def dfs(r, c):

            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 1

            if (r, c) in visited:
                return 0

            visited.add((r,c))

            res = 0
            res += dfs(r, c + 1)
            res += dfs(r, c - 1)
            res += dfs(r + 1, c)
            res += dfs(r - 1, c)

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    res += dfs(r, c)
        return res
