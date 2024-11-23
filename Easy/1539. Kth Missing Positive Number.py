class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if len(arr) == arr[-1]:
            return arr[-1] + k

        if k > (arr[-1] - len(arr)):
            return k + len(arr)

        count = 0

        for i in range(1, arr[-1] + 1):
            if i == arr[0]:
                arr.pop(0)
            else:
                count += 1
            if count == k:
                return i
