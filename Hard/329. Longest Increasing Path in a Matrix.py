class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[0] * len(matrix[0]) for i in range(len(matrix))]

        def dfs(r, c, prev, val):

            if r < 0 or c < 0 or r >= ROWS or c >= COLS or matrix[r][c] <= prev:
                return 0

            if dp[r][c] != 0:
                return dp[r][c]

            prevNode = matrix[r][c]
            
            res = max(
                dfs(r + 1, c, prevNode, val + 1),
                dfs(r - 1, c, prevNode, val + 1),
                dfs(r, c + 1, prevNode, val + 1),
                dfs(r, c - 1, prevNode, val + 1)
            ) + 1

            dp[r][c] = res

            return res

        maxLen = 0
        for r in range(ROWS):
            for c in range(COLS):
                maxLen = max(maxLen, dfs(r, c, float("-inf"), 1))

        return maxLen
