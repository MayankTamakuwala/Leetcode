class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        res = 0

        if not grid:
            return 0
        
        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    res += 1
                dfs(r, c)
        return res
