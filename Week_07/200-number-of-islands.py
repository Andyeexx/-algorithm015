def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        max_row=len(grid)
        max_col=len(grid[0])
        count=0

        def dfs(row, col):
            if row>=max_row or col>=max_col or row<0 or col<0: return
            if grid[row][col]=='0': return
            grid[row][col]='0'
            dfs(row,col+1)
            dfs(row+1,col)
            dfs(row,col-1)
            dfs(row-1,col)
        
        for i in range(max_row):
            for j in range(max_col):
                if grid[i][j]=='1':
                    count+=1
                    dfs(i,j)
        return count