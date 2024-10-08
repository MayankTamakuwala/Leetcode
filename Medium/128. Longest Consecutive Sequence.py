class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        track = set(nums)
        res = 0
        for i in nums:
            t = 1
            if i-t in track:
                continue
            else:
                while i+t in track:
                    t += 1
                res = max(t, res)
        return res
