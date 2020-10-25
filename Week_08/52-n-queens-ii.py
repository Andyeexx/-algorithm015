def totalNQueens(self, n: int) -> int:
        if not n:
            return 0
        ans=0
        def dfs(cols,pie,na):
            nonlocal ans
            if len(cols)==n:
                ans+=1
            row=len(cols)
            for i in range(n):
                if i not in cols and i+row not in pie and row-i not in na:
                    dfs(cols|{i}, pie|{i+row}, na|{row-i})
        dfs(set(),set(),set())
        return ans