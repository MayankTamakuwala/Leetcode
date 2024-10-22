class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        one, zero = 0, 0
        diff = {}
        res = 0
        for i in range(len(nums)):
            if nums[i]:
                one += 1
            else:
                zero += 1
            if one - zero not in diff:
                diff[one - zero] = i
            if one == zero:
                res = one + zero
            else:
                idx = diff[one - zero]
                res = max(res, i-idx)
        return res
