class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def helper(pos,cur):
            if(len(cur)==k): return ans.append(cur)
            for i in range(pos+1,n+1):
                helper(i,cur+[i])
        helper(0,[])
        return ans