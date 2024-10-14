class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Solution 1

        # S = len(s)
        # T = len(t)
        # if s=='': 
        #     return True
        # if S>T:
        #     return False
        # j = 0
        # for i in range(T):
        #     if(t[i]) == s[j]:
        #         if j == S-1:
        #             return True
        #         j+=1
        # return False

        # Solution 2

        if s == "":
            return True
        
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return True if i == len(s) else False