class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans,length=[],len(nums)
        def helper(valid,cur):
            if(len(cur)==length):
                ans.append(cur)
            else:   
                for i in range(len(valid)):
                    helper(valid[:i]+valid[i+1:],cur+[valid[i]])
        helper(nums,[])
        return ans