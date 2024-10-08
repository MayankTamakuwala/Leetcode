class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        s = 0
        res = 0
        for i in nums:
            s += i
            if s == 0:
                res += 1
        return res