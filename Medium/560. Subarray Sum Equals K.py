class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        track = {0: 1}
        s = 0
        res = 0
        for i in nums:
            s += i
            diff = s - k
            res += track.get(diff, 0)
            track[s] = 1 + track.get(s, 0)
        return res
