class Solution:
    def reverseWords(self, s: str) -> str:
        # Solution 1
        # words = s.split(" ")
        # res = ""

        # for i in range(len(words) - 1, -1, -1):
        #     if words[i] != "":
        #         res += words[i] + " "
        # return res[:-1]

        # Solution 2
        s = s.strip()
        return " ".join(reversed(s.split()))
