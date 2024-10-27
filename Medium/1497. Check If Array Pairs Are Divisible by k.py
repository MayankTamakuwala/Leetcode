class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if k == 1:
            return True

        track = defaultdict(int)

        for i in arr:
            rem = (i % k)
            track[rem] += 1

        if track[0] % 2 != 0:
            return False

        for i in range(1,(k+1)//2):
            diff = k - i
            if track[diff] != track[i]:
                return False

        return True
