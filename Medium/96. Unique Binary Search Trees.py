class Solution:
    def numTrees(self, n: int) -> int:

        # Solution 1

        numTree = [0] * (n + 1)
        numTree[0] = 1
        
        for nodes in range(1, n+1):
            for i in range(nodes):
                numTree[nodes] += (numTree[i] * numTree[nodes - i - 1])

        return numTree[n]

        # Solution 2
        # Observation
        # 1 => 1
        # 2 => 2
        # 3 => 5
        # 4 => 14
        # 5 => 42
        # 6 => 132
        # The Sequence resembles to Catalan Number Sequence

        # res = [ (1/(n+1)) * 2n C n ]; where C is Combination

        # mp = {}
        # def factorial(n):
        #     if n == 1 or n == 0:
        #         return 1
        #     if n in mp:
        #         return mp[n]
        #     ans = factorial(n - 1) * n
        #     mp[n] = ans
        #     return ans

        # return (factorial(2*n)//(factorial(n) ** 2))//(n+1)
