class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Solution 1
        # set1 = set(nums1)
        # set2 = set(nums2)
        # ans = [set(),set()]

        # for i in range(len(nums1)):
        #     if nums1[i] not in set2:
        #         ans[0].add(nums1[i])
        
        # for i in range(len(nums2)):
        #     if nums2[i] not in set1:
        #         ans[1].add(nums2[i])
        
        # return [list(ans[0]), list(ans[1])]

        # Solution 2
        nums1, nums2 = set(nums1), set(nums2)
        return [list(nums1-nums2), list(nums2-nums1)]
