class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l, r = 0, len(citations) - 1
        res = len(citations)
        c_len = len(citations)
        while l <= r:
            m = (l + r)//2
            if (c_len - m) == citations[m]:
                return citations[m]

            if (c_len - m) < citations[m]:
                r = m - 1
            else:
                l = m + 1

        return c_len - r -1
