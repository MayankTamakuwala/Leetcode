class Solution:
    def hIndex(self, citations: List[int]) -> int:

        # Solution 1

        # citations.sort()
        # n, i = len(citations), 1
        # while i <= n:
        #     if citations[n-i] < i: break
        #     i += 1
        # return i-1

        # Solution 2

        citations.sort(reverse = True)
        res = 1
        for i in range(len(citations)):
            if citations[i] < res:
                break
            res += 1
        return res-1
