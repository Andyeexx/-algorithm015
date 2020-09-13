class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans,length=[],len(nums)
        check=[0 for i in range(length)]
        nums.sort()

        def helper(check, cur):
            if(len(cur)==length):ans.append(cur)
            for i in range(length):
                if(check[i]==1): continue
                if(i>0 and nums[i-1]==nums[i] and check[i-1]==0): continue
                check[i]=1
                helper(check,cur+[nums[i]])
                check[i]=0
        helper(check,[])
        return ans