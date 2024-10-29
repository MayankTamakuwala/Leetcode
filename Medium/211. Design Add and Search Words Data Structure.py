class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(node, start):
            for i in range(start, len(word)):
                c = word[i]
                if c == ".":
                    for child in node.children.values():
                        if dfs(child, i + 1):
                            return True
                    return False
                elif c not in node.children:
                    return False
                node = node.children[c]
            return node.endOfWord

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)