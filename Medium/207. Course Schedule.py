class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        courseMap = collections.defaultdict(list)
        track = set()
        for i in prerequisites:
            courseMap[i[0]].append(i[1])

        def dfs(course):
            if course in track:
                return False

            if not courseMap[course]:
                return True

            track.add(course)

            for c in courseMap[course]:
                if not dfs(c):
                    return False
            track.remove(course)
            courseMap[course] = []
            return True


        for k in range(numCourses):
            if not dfs(k):
                return False
        return True
