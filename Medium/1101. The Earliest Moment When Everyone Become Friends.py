class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key = lambda x: x[0])
        friends = defaultdict(set)

        for i in range(n):
            friends[i] = {i}

        for ts, p1, p2 in logs:
            friends[p1] = friends[p1].union(friends[p2])

            for i in friends[p1]:
                friends[i] = friends[p1]
            
            if len(friends[p1]) == n:
                return ts
        
        return -1
