class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        maxNum = max(nums)

        nums = list(map(str,nums))
        nums = sorted(nums, key=lambda x: x*len(str(maxNum)), reverse=True)

        if nums[0] == "0":
            return "0"

        return "".join(nums)