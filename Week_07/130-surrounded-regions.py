def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return 
        f={}
        def find(i):
            f.setdefault(i,i)
            if f[i]!=i:
                f[i]=find(f[i])
            return f[i]
        def union(i,j):
            f[find(i)]=find(j)
        
        row,col=len(board),len(board[0])
        dummy=row*col
        for i in range(row):
            for j in range(col):
                if board[i][j]=='O':    
                    if i==0 or j==0 or i==row-1 or j==col-1:
                        union(i*col+j, dummy)
                    else:
                        for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                            if board[i+x][j+y]=='O':
                                union(i*col+j, (i+x)*col+(j+y))
        
        for i in range(row):
            for j in range(col):
                if board[i][j]=='O' and find(dummy)!=find(i*col+j):
                    board[i][j]='X'