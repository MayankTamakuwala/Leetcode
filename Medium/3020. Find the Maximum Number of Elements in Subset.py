class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)

        res = 0
        for key in counter.keys():
            if key == 1:
                total = counter[key] if counter[key] % 2 else counter[key] - 1
            else:
                total = 1
                while sqrt(key) in counter and counter[sqrt(key)] >= 2:
                    total += 2
                    key = sqrt(key)
            res = max(res, total)
        return res