import collections


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        subBox = collections.defaultdict(set)

        for r in range(0, 9):
            for c in range(0, 9):
                if board[r][c] == ".":
                    continue

                if (
                    board[r][c] in cols[c]
                    or board[r][c] in rows[r]
                    or board[r][c] in subBox[(r // 3, c // 3)]
                ):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                subBox[(r // 3, c // 3)].add(board[r][c])

        return True
