def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols=[set() for _ in range(9)]
        rows=[set() for _ in range(9)]
        matrix=[[set() for _ in range(3)]for _ in range(3)]
        for row in range(9):
            for col in range(9):
                if board[row][col]!=".":
                    char=board[row][col]
                    if (char in rows[row]) or (char in cols[col]) or char in matrix[row//3][col//3]:
                        return False
                    cols[col].add(char)
                    rows[row].add(char)
                    matrix[row//3][col//3].add(char)
        return True