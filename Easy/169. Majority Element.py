class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = maxCount = 0

        for i in nums:
            if maxCount == 0:
                res = i
            maxCount += (1 if res == i else -1)
        return res
