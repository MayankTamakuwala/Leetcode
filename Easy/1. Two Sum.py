class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsTrack = defaultdict()
        res = []

        for ind,num in enumerate(nums):
            diff = target - num
            if diff in numsTrack:
                res.append(numsTrack[diff])
                res.append(ind)
            else:
                numsTrack[num] = ind
        return res