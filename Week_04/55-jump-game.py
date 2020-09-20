def canJump(self, nums: List[int]) -> bool:
        max_l,n=0,len(nums)
        for i in range(n):
            if(i>max_l):return False
            if(i+nums[i]>max_l):
                max_l=i+nums[i]
        return True
