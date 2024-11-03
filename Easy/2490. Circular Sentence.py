class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")

        if len(words) == 1:
            if sentence[0] == sentence[-1]:
                return True
            return False

        prev = words[0]
        for i in range(1, len(words)):
            if prev[-1] != words[i][0]:
                return False
            prev = words[i]
        prev = words[-1]
        if prev[-1] == words[0][0]:
            return True
        return False
