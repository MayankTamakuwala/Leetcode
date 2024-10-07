class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        merged = ""
        l1, l2 = len(word1), len(word2)
        max_len = max(l1, l2)
        for i in range(max_len):
            if i < l1:
                merged+=word1[i]
            if i < l2:
                merged+=word2[i]
        return merged