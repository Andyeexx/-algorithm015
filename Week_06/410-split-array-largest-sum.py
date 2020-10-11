def splitArray(self, nums: List[int], m: int) -> int:
        if not nums or not m: return 0
        left ,right = max(nums), sum(nums)
        def test_m(mid):
            count,s=1,0
            for num in nums:
                if(s+num)>mid:
                    s=num
                    count+=1
                else:
                    s+=num
            return count>m
        
        while(left<right):
            mid=(left+right)//2
            if(test_m(mid)):
                left=mid+1
            else:
                right=mid
        return right