class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c, idx):
            if idx == len(word):
                return True

            if (r,c) in visited or r < 0 or c < 0 or r >= ROWS or c >= COLS or word[idx] != board[r][c]:
                return False
            
            visited.add((r,c))
            newIdx = idx + 1
            res = dfs(r + 1, c, newIdx) or dfs(r - 1, c, newIdx) or dfs(r, c + 1, newIdx) or dfs(r, c - 1, newIdx)
            visited.remove((r,c))

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c , 0):
                    return True
        return False
