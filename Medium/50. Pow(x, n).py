class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Approach: Power My solution
        # O(n) time and O(1) memory

        # if n > 0:
        #     return x**n
        # else:
        #     return (1/x)**(abs(n))

        # # Approach: Divide and Conquer Algorithm (Recursive)
        # # O(log n) time and O(1) memory

        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            res = helper(x, n//2)
            res *= res
            return x*res if n%2 else res

        res = helper(x,abs(n))
        return res if n >= 0 else 1/res
