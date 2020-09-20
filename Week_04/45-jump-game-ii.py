def jump(self, nums: List[int]) -> int:
        max_l,n=0,len(nums)
        end,count=0,0
        for i in range(n-1):
            if(i>max_l):return -1
            if(i+nums[i]>max_l):
                max_l=i+nums[i]
            if(i==end):
                end=max_l
                count+=1
        return count