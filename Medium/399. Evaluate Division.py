class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)

        for i in range(len(equations)):
            a, b =  equations[i]
            adjList[a].append([b, values[i]])
            adjList[b].append([a, 1/values[i]])

        def findPath(src, dest):
            if src not in adjList or dest not in adjList:
                return -1
            queue, visited = [], set()

            visited.add(src)
            queue.append([src, 1])
            while queue:
                node, val = queue.pop(0)
                if node == dest:
                    return val

                for neig, neigVal in adjList[node]:
                    if neig not in visited:
                        queue.append([neig, neigVal * val])
                        visited.add(neig)
            return -1

        return [findPath(q[0], q[1]) for q in queries]
