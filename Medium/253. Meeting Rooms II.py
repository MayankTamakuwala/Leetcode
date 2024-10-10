class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []

        for i in intervals:
            start.append(i[0])
            end.append(i[1])

        start.sort()
        end.sort()

        p1 = p2 = 0
        res = count = 0
        while p1 < len(start) and p2 < len(end):
            if(start[p1] < end[p2]):
                count += 1
                res = max(count, res)
                p1 += 1
            else:
                count -= 1
                p2 += 1
        return res
