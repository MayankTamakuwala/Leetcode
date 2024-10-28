class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        freq = [[0] * 26]

        for c in s:
            freq.append(freq[-1].copy())
            freq[-1][ord(c) - ord('a')] += 1

        res = []

        for left,right in queries:
            total = 0
            freq_left = freq[left]
            freq_right = freq[right+1] 
            for i in range(26):
                diff = freq_right[i] - freq_left[i]
                total += diff * (diff +1) //2
            res.append(total)
        return res
