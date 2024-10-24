class Solution:
    def minSwaps(self, s: str) -> int:
        maxBracs, count = float('-inf'), 0

        for i in s:
            if i == "]":
                count += 1
            else:
                count -= 1
            maxBracs = max(maxBracs, count)
        
        return (maxBracs + 1)//2
