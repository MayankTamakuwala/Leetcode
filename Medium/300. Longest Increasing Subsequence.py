from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # Solution 1

        subSeq = []

        for i in nums:
            idx = bisect_left(subSeq, i)
            if idx == len(subSeq):
                subSeq.append(i)
            else:
                subSeq[idx] = i
        return len(subSeq)

        # Solution 2

        # LIS = [1] * len(nums)

        # for i in range(len(nums) - 1, -1, -1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] < nums[j]:
        #             LIS[i] = max(LIS[i], 1 + LIS[j])
        
        # return max(LIS)
