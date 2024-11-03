class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # # Approach: Linear Scan
        # # O(n) time and O(n) memory
        
        # # Pad 0 to prevent edge cases
        flowerbed.append(0)
        flowerbed.insert(0, 0)

        for i in range(1, len(flowerbed) - 1):
            if n <= 0:
                break
            elif not flowerbed[i] and not flowerbed[i-1] and not flowerbed[i+1]:
                flowerbed[i] = 1
                n -= 1
        return not n
