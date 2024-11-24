class Solution:

    def __init__(self, w: List[int]):
        s = 0
        self.prefix = []
        for i in w:
            t = i+s
            self.prefix.append(t)
            s = t

    def pickIndex(self) -> int:
        r = random.uniform(0, self.prefix[-1])
        return bisect.bisect_left(self.prefix, r)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
