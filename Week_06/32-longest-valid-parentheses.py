def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        ans=0
        dp=[0]*len(s)
        for i in range(1,len(s)):
            if s[i]==')':
                if(s[i-1]=='('):
                    dp[i]=dp[i-2]+2
                else:
                    if(i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=='('):
                        dp[i]=dp[i-1]+dp[i-dp[i-1]-2]+2
                ans=max(ans,dp[i])
        return ans