class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        pivot = 0
        check = False
        for i in range(len(nums) - 2, -1 , -1):
            if nums[i+1] > nums[i]:
                pivot = i + 1
                break

        if pivot == 0:
            nums.sort()
            return

        if pivot == len(nums) - 1:
            nums[-1], nums[-2] = nums[-2], nums[-1]
            return

        p2 = 0
        pivotVal = nums[pivot-1]
        diff = float('inf')
        for i in range(pivot,len(nums)):
            t = nums[i] - pivotVal
            if t > 0 and t < diff:
                diff = t
                p2 = i

        nums[p2], nums[pivot - 1] = nums[pivot - 1], nums[p2]
        nums[pivot:] = sorted(nums[pivot:])
