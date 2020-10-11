def canCross(self, stones: List[int]) -> bool:
        n=len(stones)
        dp=[set() for _ in range(n)]
        dp[0].add(0)
        for i in range(n):
            for j in range(i):
                need= stones[i]-stones[j]
                if(need-1 in dp[j] or need+1 in dp[j] or need in dp[j]):
                    dp[i].add(need)
        return len(dp[-1])>0