class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        rightMax = [0]*len(nums)
        prev = nums[-1]
        for i in range(len(nums)-1, -1, -1):
            rightMax[i] = max(nums[i], prev)
            prev = rightMax[i]
        
        res = 0
        i = 0
        for j in range(1,len(nums)):
            if rightMax[j] >= nums[i]:
                res = max(res, j-i)
            else:
                i += 1

        return res
