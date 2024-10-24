class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        a_idx, b_idx, res = [], [], []

        rangeValue = len(s) - min(len(a), len(b)) + 1
        for i in range(rangeValue):
            if s[i:i+len(a)] == a:
                a_idx.append(i)
            if s[i:i+len(b)] == b:
                b_idx.append(i)
        
        if len(a_idx) == 0 or len(b_idx) == 0:
            return []

        i, j = 0, 0

        while i<len(a_idx) and j<len(b_idx):
            if abs(a_idx[i] - b_idx[j]) <= k:
                res.append(a_idx[i])
                i += 1
            elif a_idx[i] < b_idx[j]:
                i += 1
            else:
                j += 1

        return res
