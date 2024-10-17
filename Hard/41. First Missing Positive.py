class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums):
            print(i, nums[i])
            if nums[i] <= 0:
                i += 1
            elif nums[i] < len(nums) and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1
        
        res = 1

        for i in nums:
            if i == res:
                res += 1
        return res
