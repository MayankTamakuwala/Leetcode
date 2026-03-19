# 763. Partition Labels
# Medium
# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

# Example 1:

# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
# Example 2:

# Input: s = "eccbbbbdec"
# Output: [10]

# Constraints:

# 1 <= s.length <= 500
# s consists of lowercase English letters.

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letters = len(set(s))
        adj_list = [[-1,-1] for _ in range(26)]

        for j, i in enumerate(s):
            l = ord(i) - ord("a")
            if adj_list[l][0] == -1:
                adj_list[l][0] = j
                adj_list[l][1] = j
            else:
                adj_list[l][1] = j

        intervals = sorted(adj_list)
        intervals = intervals[26 - letters:]
        merge = [intervals[0]]

        for interval in intervals[1:]:
            if merge[-1][1] > interval[0]:
                merge[-1][1] = max(merge[-1][1], interval[1])
            else:
                merge.append(interval)
        return [end - start + 1 for start, end in merge]

o = Solution()

s = "eccbbbbdec"
print(o.partitionLabels(s))
