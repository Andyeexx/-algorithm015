def generateParenthesis(self, n: int) -> List[str]:
        if not n:return ans
        dp=[]
        dp.append([""])
        dp.append(["()"])
        for i in range(2,n+1):
            l=[]
            for j in range(i):
                for k1 in dp[j]:
                    for k2 in dp[i-1-j]:
                        l.append( "(" + k1 + ")" +k2 )
            dp.append(l)
        return dp[n]