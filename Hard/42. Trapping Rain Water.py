class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]

        while l<r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                area += (maxL - height[l]) if (maxL - height[l]) >= 0 else 0
            else:
                r -= 1
                maxR = max(maxR, height[r])
                area += (maxR - height[r]) if (maxR - height[r]) >= 0 else 0
        return area
