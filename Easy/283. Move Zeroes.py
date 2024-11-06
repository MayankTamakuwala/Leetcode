class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 1

        if len(nums) <= 1:
            return nums
        while r < len(nums):
            if nums[l] == 0 and nums[r] != 0:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
                r += 1
            elif nums[l] != 0 and nums[r] != 0 or nums[l] != 0 and nums[r] == 0:
                l += 1
                r += 1
            else:
                r += 1
