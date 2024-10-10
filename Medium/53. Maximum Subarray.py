class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float(-inf)
        t = 0
        for i in nums:
            t += i
            maxSum = max(maxSum, t)
            if t < 0:
                t = 0
        return maxSum