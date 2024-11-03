class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1
        strList = list(s)

        vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}

        while l < r:
            if strList[l] in vowels and strList[r] in vowels:
                strList[l], strList[r] = strList[r], strList[l]
                l += 1
                r -= 1
            if strList[l] not in vowels:
                l += 1
            if strList[r] not in vowels:
                r -= 1
        return ''.join(strList)
