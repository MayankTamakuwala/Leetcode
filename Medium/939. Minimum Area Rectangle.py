class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # Solution 1
        points.sort(key = lambda x: x[1])
        y = defaultdict(list)
        x = defaultdict(list)
        diff = []
        for i in points:
            y[i[1]].append(i[0])
        for i in points:
            x[i[0]].append(i[1])

        prev = points[0][0]
        for i in points[1:]:
            diff.append(i[0] - prevN)
            prev = i[0]
        return 0
    
        # Solution 2
        # visited = set()
        # area = float('inf')

        # for x1, y1 in points:
        #     for x2, y2 in visited:
        #         if (x1, y2) in visited and (x2, y1) in visited:
        #             a = abs(x2 - x1) * abs(y2 - y1)
        #             area = min(a, area)
        #     visited.add((x1,y1))
        
        # return 0 if area == float('inf') else area
