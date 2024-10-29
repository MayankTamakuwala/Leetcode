import collections

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Approach: Djikstra's Algorithm
        # O(E * log V) time

        # Create an adjacency list
        # Create dictionary or hashmap of edges

        edges = defaultdict(list)
                
        for u,v,w in times:
            edges[u].append((v,w))

        visited = set()

        minHeap = [(0, k)]
        heapq.heapify(minHeap)

        res = 0

        while minHeap:

            time, destNode = heapq.heappop(minHeap)

            if destNode in visited:
                continue

            visited.add(destNode)
            res = max(time, res)

            for neighNode, neighTime in edges[destNode]:
                if neighNode not in visited:
                    heapq.heappush(minHeap, (neighTime + time, neighNode))

        return res if len(visited) == n else -1
