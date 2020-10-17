import copy
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        cols=[set() for _ in range(9)]
        rows=[set() for _ in range(9)]
        matrix=[[ set() for _ in range(3) ] for _ in range(3)]
        count=0
        for i in range(len(board)):
            row=board[i]
            for j in range(len(row)):
                if(row[j]!="."):
                    cols[j].add(row[j])
                    rows[i].add(row[j])
                    matrix[i//3][j//3].add(row[j])
                    count+=1
        result=None
        def helper(cols,rows,matrix,count,newboard):
            if(count==81):
                nonlocal result
                result=deepcopy(newboard)
            flag=False
            for row in range(9):
                if(flag):
                    break
                for col in range(9):
                    if(newboard[row][col]=="."):
                        for num in range(1,10,1):
                            if(str(num) in cols[col] or (str(num) in rows[row]) or (str(num) in matrix[row//3][col//3])  ):
                                continue
                            else:
                                cols[col].add(str(num))
                                rows[row].add(str(num))
                                matrix[row//3][col//3].add(str(num))
                                newboard[row][col]=str(num)
                                helper(cols,rows,matrix,count+1,newboard)
                                cols[col].remove(str(num))
                                rows[row].remove(str(num))
                                matrix[row//3][col//3].remove(str(num))
                                newboard[row][col]="."
                        flag=True
                        break
        helper(cols,rows,matrix,count, board)
        for i in range(9):
            for j in range(9):
                board[i][j]=result[i][j]