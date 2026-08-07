class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqs = defaultdict(set)

        for y in range(len(board)):
            for x in range(len(board[0])):
                if(board[y][x] == "."):
                    continue
                if(board[y][x] in rows[x] or
                    board[y][x] in cols[y] or
                    board[y][x] in sqs[(y//3, x//3)]):
                    return False
                else:
                    rows[x].add(board[y][x])
                    cols[y].add(board[y][x])
                    sqs[(y//3, x//3)].add(board[y][x])

        return True