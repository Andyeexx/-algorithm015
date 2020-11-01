def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        n=len(nums)
        ans=1
        dp=[1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j] and dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1
                if dp[i]>ans:
                    ans=dp[i]
        return ans