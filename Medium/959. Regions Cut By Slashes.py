class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        ROW1, COL1 = len(grid), len(grid)
        ROW2, COL2 = 3 * len(grid), 3 * len(grid)
        grid2 = [[0] * COL2 for _ in range(ROW2)]

        for r in range(ROW1):
            for c in range(COL1):
                r2, c2 = 3 * r, 3 * c
                if grid[r][c] == "/":
                    grid2[r2][c2 + 2] = 1
                    grid2[r2 + 1][c2 + 1] = 1
                    grid2[r2 + 2][c2] = 1
                elif grid[r][c] == "\\":
                    grid2[r2][c2] = 1
                    grid2[r2 + 1][c2 + 1] = 1
                    grid2[r2 + 2][c2 + 2] = 1

        def dfs(r, c, visited):
            if (r < 0 or c < 0 or r == ROW2 or c == COL2 or grid2[r][c] != 0 or (r,c) in visited):
                return
            visited.add((r,c))
            dfs(r + 1, c, visited)
            dfs(r - 1, c, visited)
            dfs(r, c + 1, visited)
            dfs(r, c - 1, visited)

        res = 0
        visited = set()
        for r in range(ROW2):
            for c in range(COL2):
                if grid2[r][c] == 0 and (r,c) not in visited:
                    dfs(r, c, visited)
                    res += 1
        return res
