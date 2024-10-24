class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        i, j = 0, k
        res = []
        while j <= len(nums):
            counter = Counter(nums[i:j])
            t = 0
            if x >= len(counter):
                for c in counter:
                    t += counter[c]*c
            else:
                sorted_counter = sorted(counter.items(), key = lambda x: (x[1], x[0]), reverse=True)
                for c in range(x):
                    t += sorted_counter[c][1]*sorted_counter[c][0]
            res.append(t)
            i += 1
            j += 1
        return res
