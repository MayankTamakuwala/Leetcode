class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Approach:
        # O(n) time 

        total = sum(nums) #O(n) time
        lsum = 0

        for i in range(len(nums)):
            rsum = total - lsum - nums[i]
            if lsum == rsum:
                return i
            lsum += nums[i]
        return -1
