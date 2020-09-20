def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if(not board or not click): return board
        row,col=click[0],click[1]
        max_row,max_col=len(board),len(board[0])
        def helper(row,col):
            if(board[row][col]!='E' and board[row][col]!='M'): return
            if(board[row][col]=='M'):
                board[row][col]='X'
                return
            direction=[(row-1,col),(row-1,col+1),(row,col+1),(row+1,col+1),(row+1,col),(row+1,col-1),(row,col-1),(row-1,col-1)]
            mine_count=0
            next_recursion=[]
            for (r,c) in direction:
                if(0<=r and r<max_row and 0<=c and c<max_col):
                    if(board[r][c]=='M' or board[r][c]=='X'):
                        mine_count+=1
                    next_recursion.append((r,c))
            if(mine_count!=0):
                board[row][col]=str(mine_count)
            else:
                board[row][col]='B'
                for (r,c) in next_recursion:
                    helper(r,c)
        helper(row,col)        
        return board