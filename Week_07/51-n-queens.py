def solveNQueens(self, n: int) -> List[List[str]]:
        if not n: return []
        cols,pie,na=set(),set(),set()
        ans=[]
        def dfs(tmp,cols,pie,na):
            if len(cols)==n:
                ans.append(tmp)
            for col in range(n):
                row=len(cols)
                if (col not in cols) and (col+row not in pie) and (row-col not in na):
                    dfs(tmp+["."*(col) + "Q" + "."*(n-col-1)],cols|{col},pie|{col+row},na|{row-col})      
        dfs([],cols,pie,na)
        return ans