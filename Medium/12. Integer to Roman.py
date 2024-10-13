class Solution:
    def intToRoman(self, num: int) -> str:
        romanMap = { 
            1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C",
            90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 8: "VIII",
            7: "VII", 6: "VI", 5: "V", 4: "IV", 3: "III", 2: "II", 1: "I"
        }
        
        keys = list(romanMap.keys())

        i = 0
        dig = []
        res = ""
        while num > 0:
            x = num - keys[i]
            if x < 0:
                i += 1
            else:
                num = x
                dig.append(keys[i])

        for i in dig:
            res += romanMap[i]
        return res