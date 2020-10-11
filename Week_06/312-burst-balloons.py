def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0,1)
        nums.append(1)
        dp=[[0]*len(nums) for _ in range(len(nums))]
        def localmax(i,j):
            m=0
            for k in range(i+1,j):
                tmp=dp[i][k]+dp[k][j]+nums[i]*nums[j]*nums[k]
                if tmp>m:
                    m=tmp
            return m

        for n in range(2,len(nums)):
            for i in range(len(nums)-n):
                dp[i][i+n]=max(dp[i][i+n],localmax(i,i+n))
        return dp[0][len(nums)-1]