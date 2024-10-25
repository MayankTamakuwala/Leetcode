class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Solution 1
        # maxNum = max(nums)

        # nums = list(map(str,nums))
        # nums = sorted(nums, key=lambda x: x*len(str(maxNum)), reverse=True)

        # if nums[0] == "0":
        #     return "0"

        # return "".join(nums)
    
        #Solution 2
        nums = list(map(str,nums))

        def mergeSort(nums):
            if len(nums) == 1:
                return nums
            m = len(nums)//2
            l_arr = mergeSort(nums[:m])
            r_arr = mergeSort(nums[m:])
            return merge(l_arr, r_arr)

        def merge(l, r):
            p1, p2 = 0, 0
            merged = []
            while p1 < len(l) and p2 < len(r):
                if (l[p1]+r[p2]) < (r[p2]+l[p1]):
                    merged.append(r[p2])
                    p2 += 1
                elif (l[p1]+r[p2]) > (r[p2]+l[p1]):
                    merged.append(l[p1])
                    p1 += 1
                else:
                    merged.append(l[p1])
                    merged.append(r[p2])
                    p1 += 1
                    p2 += 1
            
            while p1 < len(l):
                merged.append(l[p1])
                p1 += 1
            
            while p2 < len(r):
                merged.append(r[p2])
                p2 += 1
            return merged
        
        nums = mergeSort(nums)

        if nums[0] == "0":
            return "0"

        return "".join(nums)
