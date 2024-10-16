class NumArray:

    def __init__(self, nums: List[int]):
        self.range = []
        prev = 0
        for i in nums:
            s = prev + i
            self.range.append(s)
            prev = s

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.range[right] - self.range[left - 1]
        else:
            return self.range[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)