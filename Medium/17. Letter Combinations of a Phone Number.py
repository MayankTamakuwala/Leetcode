from itertools import combinations
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(letters[digits[0]])

        def backtrack(i, curStr):
            if len(curStr) == len(digits) :
                res.append(curStr)
                return
            for c in letters[digits[i]]:
                backtrack(i + 1, curStr + c)

        backtrack(0, "")
        return res
