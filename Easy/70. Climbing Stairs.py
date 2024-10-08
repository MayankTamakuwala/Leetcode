class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2 or n == 3:
            return n
        r1 = 2
        r2 = 3
        res = 0
        for i in range(4, n+1):
            res = r1 + r2
            r1 = r2
            r2 = res
        return res