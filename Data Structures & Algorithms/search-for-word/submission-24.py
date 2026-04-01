class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        S = word[0]
        global path
        path = set()
        def dfs(x, y, idx):
            if x >= len(board) or x < 0:
                return False
            if y >= len(board[0]) or y < 0:
                return False
            if idx >= len(word):
                return False
            if board[x][y] != word[idx]:
                return False
            if (x,y) in path:
                return False
            if idx == len(word) - 1:
                print(idx, word, x, y)
                return True
            
            path.add((x,y))
            res = dfs(x + 1, y, idx + 1) or dfs(x, y + 1, idx + 1) or dfs(x - 1, y, idx + 1) or dfs(x, y - 1, idx + 1)
            if res:
                return True
            path.remove((x,y))

        for x, row in enumerate(board):
            for y, char in enumerate(row):
                if char == S:
                    path = set()
                    matches = dfs(x, y, 0)
                    if matches:
                        return True
        return False
