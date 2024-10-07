class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        prev = res = 0

        for val in target:
            if val > prev:
                res += val - prev
            prev = val
        return res