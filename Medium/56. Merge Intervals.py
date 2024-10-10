class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals, key = lambda x: x[1])
        merged = [intervals[0]]
        for i in intervals:
            last_merged = merged[-1]
            if last_merged[1] >= i[0]:
                merged[-1][1] = max(i[1], last_merged[1])
            else:
                merged.append(i)
        
        return merged
