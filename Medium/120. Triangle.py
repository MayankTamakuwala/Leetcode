class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle) + 1)

        for row in triangle[::-1]:
            for idx, val in enumerate(row):
                dp[idx] = val + min(dp[idx], dp[idx + 1])

        return dp[0]
