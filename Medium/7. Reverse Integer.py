class Solution:
    def reverse(self, x: int) -> int:
        
        # Solution 1
        
        # MIN = -2147483648
        # MAX = 2147483647
        # res = 0

        # while x:
        #     digit = int(math.fmod(x,10))
        #     x = int(x / 10)

        #     if (res > MAX//10 or (res == MAX//10 and digit >= MAX%10)):
        #         return 0

        #     if (res < MIN//10 or (res == MIN//10 and digit <= MIN%10)):
        #         return 0
            
        #     res = (res * 10) + digit
        #     print(res)
        
        # return res
        
        # Solution 2
        MIN = -2147483648
        MAX = 2147483647
        res = 0
        isNeg = x<0
        x = (x*-1) if isNeg else x
        while x:
            rem = int(math.fmod(x,10))
            x = x//10
            res = (res * 10) + rem
            print(res)
            if res < MIN or res > MAX:
                return 0
        res = (res * -1) if isNeg else res

        if res < MIN or res > MAX:
            return 0
        return res
