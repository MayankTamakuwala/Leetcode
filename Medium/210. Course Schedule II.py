class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        courseMap = defaultdict(list)

        for c1, c2 in prerequisites:
            courseMap[c1].append(c2)
        
        visited, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False

            if course in visited:
                return True
            
            cycle.add(course)

            for c in courseMap[course]:
                if not dfs(c):
                    return False
            visited.add(course)
            cycle.remove(course)
            res.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return res
