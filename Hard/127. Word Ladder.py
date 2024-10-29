class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        adjList = defaultdict(list)

        for word in wordList:
            for c in range(len(word)):
                key = word[:c] + "*" + word[c+1:]
                adjList[key].append(word)


        res = 1
        queue = [beginWord]
        wordsVisited = set([beginWord])

        while queue:
            queue_length = len(queue)
            for i in range(queue_length):
                word = queue.pop(0)
                if word == endWord:
                    return res
                for c in range(len(word)):
                    key = word[:c] + "*" + word[c+1:]
                    for neigbr in adjList[key]:
                        if neigbr not in wordsVisited:
                            wordsVisited.add(neigbr)
                            queue.append(neigbr)
            res += 1
        return 0
