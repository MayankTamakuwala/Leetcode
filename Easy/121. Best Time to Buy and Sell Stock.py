class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minVal, maxProfit = float(inf), 0

        for i in prices:
            if i <= minVal:
                minVal = i
            else:
                p = i - minVal
                maxProfit = max(p, maxProfit)
        return maxProfit