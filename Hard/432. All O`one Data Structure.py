class Node:
    def __init__(self):
        self.freq = None
        self.prev = None
        self.next = None
        self.keys = []


class AllOne:

    def __init__(self):
        self.nodeMap = {}
        self.freqMap = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        if key in self.nodeMap:
            keyNode = self.nodeMap[key]
            keyOldFreq = keyNode.freq
            self.freqMap[keyOldFreq].keys.remove(key)

            if len(self.freqMap[keyOldFreq].keys) == 0:
                freqPrev = self.freqMap[keyOldFreq].prev
                freqNext = self.freqMap[keyOldFreq].next
                freqPrev.next = freqNext
                freqNext.prev = freqPrev
                keyNode = keyNode.prev
                del self.freqMap[keyOldFreq]

            if keyOldFreq + 1 in self.freqMap:
                self.freqMap[keyOldFreq + 1].keys.append(key)
                self.nodeMap[key] = self.freqMap[keyOldFreq + 1]

            else:
                newNode = Node()
                newNode.freq = keyOldFreq + 1
                newNode.keys.append(key)

                keyNodeNext = keyNode.next
                newNode.prev = keyNode
                newNode.next = keyNodeNext
                keyNodeNext.prev = newNode
                keyNode.next = newNode

                self.nodeMap[key] = newNode
                self.freqMap[keyOldFreq + 1] = newNode

        else:

            if 1 in self.freqMap:
                self.freqMap[1].keys.append(key)
                self.nodeMap[key] = self.freqMap[1]

            else:
                newNode = Node()
                newNode.freq = 1
                newNode.keys.append(key)

                headNext = self.head.next

                newNode.prev = self.head
                newNode.next = headNext
                headNext.prev = newNode
                self.head.next = newNode

                self.nodeMap[key] = newNode
                self.freqMap[1] = newNode

    def dec(self, key: str) -> None:
        keyNode = self.nodeMap[key]
        keyOldFreq = keyNode.freq
        self.freqMap[keyOldFreq].keys.remove(key)

        if keyOldFreq > 1:
            if (keyOldFreq - 1) in self.freqMap:
                self.freqMap[keyOldFreq].prev.keys.append(key)
                self.nodeMap[key] = self.freqMap[keyOldFreq].prev
            else:
                newNode = Node()
                newNode.freq = keyOldFreq - 1
                newNode.keys.append(key)

                keyNodePrev = keyNode.prev
                newNode.next = keyNode
                newNode.prev = keyNodePrev
                keyNodePrev.next = newNode
                keyNode.prev = newNode

                self.nodeMap[key] = newNode
                self.freqMap[keyOldFreq - 1] = newNode
        else:
            del self.nodeMap[key]

        if len(self.freqMap[keyOldFreq].keys) == 0:
            freqPrev = self.freqMap[keyOldFreq].prev
            freqNext = self.freqMap[keyOldFreq].next
            freqPrev.next = freqNext
            freqNext.prev = freqPrev
            del self.freqMap[keyOldFreq]

    def getMaxKey(self) -> str:
        t = self.tail.prev
        if len(t.keys) == 0:
            return ""
        return t.keys[0]

    def getMinKey(self) -> str:
        h = self.head.next
        if len(h.keys) == 0:
            return ""
        return h.keys[0]

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
