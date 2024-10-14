class Solution:
    def romanToInt(self, s: str) -> int:
        
        # Solution 1

        # d = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        # sum= 0
        # n = len(s)
        # i =0
        # while i<n:
        #     if i<n-1 and d[s[i]]< d[s[i+1]]:
        #         sum+=d[s[i+1]]-d[s[i]]
        #         i+=2
        #     else:
        #         sum+=d[s[i]]
        #         i+=1
        # return sum

        # Solution 2

        intMap = { 
            "M": 1000, "CM": 900,  "D": 500, "CD": 400, "C": 100, "XC": 90, 
            "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1
        }

        i = 0
        rem = ""
        res = 0
        for j,l in enumerate(s):
            if j == len(s) - 1:
                if rem:
                    rem += l
                    res += intMap[rem]
                else:
                    res += intMap[l]
            else:
                if intMap[s[j]] < intMap[s[j+1]]:
                    rem += l
                else:
                    if rem:
                        rem += l
                        res += intMap[rem]
                        rem = ""
                    else:
                        res += intMap[l]
        return res
