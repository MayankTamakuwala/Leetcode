# 14. Longest Common Prefix
# Easy
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key = lambda x:len(x))
        short_str = strs[0]

        res = ""

        for c in short_str:
            trip = False
            for s in strs[1:]:
                if not s.startswith(res + c):
                    trip = True
                    break
            if trip:
                break
            else:
                res += c
        return res
