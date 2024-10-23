class Solution:
    def maximumSwap(self, num: int) -> int:
        numStr = list(str(num))
        maxArr = ['0']*len(numStr)
        prev = '0'
        for i in range(len(numStr) - 1, -1, -1):
            maxArr[i] = max(prev, numStr[i])
            prev = maxArr[i]
        
        l, r = 0, len(numStr) - 1
        for i in range(len(numStr)):
            if numStr[i] == maxArr[i]:
                continue
            else:
                l = i
                break
        
        for i in range(len(numStr) - 1, -1, -1):
            if maxArr[i] == maxArr[l]:
                r = i
                break
        
        numStr[l], numStr[r] = numStr[r], numStr[l]

        return int(''.join(numStr))
