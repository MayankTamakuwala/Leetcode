class Solution:
    def isHappy(self, n: int) -> bool:
        track = set()

        while n not in track:
            track.add(n)
            if n == 1:
                break
            t = 0
            while n > 0:
                x = n%10
                t += (x ** 2)
                n = n//10
            n = t
        
        return True if 1 in track else False
