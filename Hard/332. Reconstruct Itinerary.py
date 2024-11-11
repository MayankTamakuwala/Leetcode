class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)
        res=[]

        for t in tickets:
            adjList[t[0]].append(t[1])

        for k in adjList:
            adjList[k].sort()

        visited = set()

        def dfs(node):

            if node in visited:
                return

            while adjList[node]:
                neig = adjList[node].pop(0)
                dfs(neig)
            
            res.append(node)

        dfs("JFK")
        return res[::-1]
