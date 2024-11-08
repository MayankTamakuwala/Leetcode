class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAlt = 0
        res = [0]

        for g in gain:
            s = res[-1] + g
            maxAlt = max(maxAlt, s)
            res.append(s)
        
        return maxAlt
