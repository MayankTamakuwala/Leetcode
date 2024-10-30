class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        rows, cols = len(rooms), len(rooms[0])
        queue = []
        visited = set()

        def addRoom(r, c):
            if (r, c) in visited or r < 0 or c < 0 or r >= rows or c >= cols or rooms[r][c] == -1:
                return

            visited.add((r, c))
            queue.append((r, c))

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))

        dist = 0
        while queue:
            queue_length = len(queue)

            for i in range(queue_length):
                r, c = queue.pop(0)
                rooms[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c - 1)
                addRoom(r, c + 1)

            dist += 1
