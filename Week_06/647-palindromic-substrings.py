def countSubstrings(self, s: str) -> int:
        if not s : return 0
        dp=[[False]*len(s) for _ in range(len(s))]
        ans=0
        for i in range(len(s)):
            for j in range(0,i+1):
                if(i-j==0):
                    dp[j][i]= True
                    ans+=1
                elif(i-j==1 and s[i]==s[j]):
                    dp[j][i]=True
                    ans+=1
                elif(i-j>1 and s[i]==s[j] and dp[j+1][i-1]==True):
                    dp[j][i]=True
                    ans+=1
        return ans
        