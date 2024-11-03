class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        currMax = max(candies)

        for c in candies:
            if c + extraCandies >= currMax:
                res.append(True)
            else:
                res.append(False)
        return res
