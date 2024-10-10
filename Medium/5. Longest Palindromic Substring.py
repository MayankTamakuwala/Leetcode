class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Solution 1

        # n = len(s)
        # dp = [[False] * n for _ in range(n)]
        # ans = [0, 0]
        
        # for i in range(n):
        #     dp[i][i] = True
        
        # for i in range(n - 1):
        #     if s[i] == s[i + 1]:
        #         dp[i][i + 1] = True
        #         ans = [i, i + 1]

        # for diff in range(2, n):
        #     for i in range(n - diff):
        #         j = i + diff
        #         if s[i] == s[j] and dp[i + 1][j - 1]:
        #             dp[i][j] = True
        #             ans = [i, j]

        # i, j = ans
        # return s[i:j + 1]

        # Solution 2

        maxLen = 0
        res = ""
        for i in range(len(s)):
            r, l = i, i

            while l >= 0 and r < len(s) and s[r] == s[l]:
                if (r-l+1) > maxLen:
                    maxLen = r-l+1
                    res = s[l:r+1]
                l -= 1
                r += 1
            
            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[r] == s[l]:
                if (r-l+1) > maxLen:
                    maxLen = r-l+1
                    res = s[l:r+1]
                l -= 1
                r += 1
        return res
        