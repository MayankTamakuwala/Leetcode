class Node:
    def __init__(self):
        self.freq = None
        self.prev = None
        self.next = None
        self.keys = []


class AllOne:

    def __init__(self):
        self.nodeMap = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        if key in self.nodeMap:
            keyNode = self.nodeMap[key]
            keyOlfFreq = keyNode.freq
            keyNode.keys.remove(key)

            if keyNode.next.freq == keyOlfFreq + 1:
                keyNode.next.keys.append(key)
                self.nodeMap[key] = keyNode.next
            else:
                newNode = Node()
                newNode.freq = keyOlfFreq + 1
                newNode.keys.append(key)

                keyNodeNext = keyNode.next
                newNode.prev = keyNode
                newNode.next = keyNodeNext
                keyNodeNext.prev = newNode
                keyNode.next = newNode
                self.nodeMap[key] = newNode
            
            if len(keyNode.keys) == 0:
                keyNodePrev = keyNode.prev
                keyNodeNext = keyNode.next

                keyNodePrev.next = keyNodeNext
                keyNodeNext.prev = keyNodePrev
        else:
            headNext = self.head.next

            if headNext.freq == 1:
                headNext.keys.append(key)
                self.nodeMap[key] = headNext
            else:
                newNode = Node()
                newNode.freq = 1
                newNode.keys.append(key)

                newNode.prev = self.head
                newNode.next = headNext
                headNext.prev = newNode
                self.head.next = newNode
                self.nodeMap[key] = newNode
                

    def dec(self, key: str) -> None:
        keyNode = self.nodeMap[key]
        keyOldFreq = keyNode.freq
        keyNode.keys.remove(key)
        
        if keyNode.freq > 1:
            keyNodePrev = keyNode.prev

            if keyNodePrev.freq == keyOldFreq - 1:
                keyNodePrev.keys.append(key)
                self.nodeMap[key] = keyNodePrev
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

        else:
            del self.nodeMap[key]
        
        if len(keyNode.keys) == 0:
            keyNodePrev = keyNode.prev
            keyNodeNext = keyNode.next

            keyNodePrev.next = keyNodeNext
            keyNodeNext.prev = keyNodePrev

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
