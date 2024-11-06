class Solution:
    def compress(self, chars: List[str]) -> int:
        l, r = 0, 1
        while r < len(chars):
            if chars[r - 1] == chars[r]:
                r += 1
            else:
                c = r - l
                if c > 1:
                    chars[l + 1 : r] = list(str(c))
                    l += 2 
                    r = l + 1
                else:
                    l = r
                    r = r + 1
        c = r - l
        if c > 1:
            chars[l + 1 : r] = list(str(c))
