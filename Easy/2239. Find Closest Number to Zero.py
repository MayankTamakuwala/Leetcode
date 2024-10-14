class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dist = float("inf")
        res = 0
        for i in nums:
            currDist = abs(i)
            if currDist < dist:
                dist = abs(i)
                res = i
            elif currDist == dist:
                if i > res:
                    res = i
        return res