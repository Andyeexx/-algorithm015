class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if(k==0):
            return []
        dic={}
        for num in nums:
            if(not dic.get(num)):
                dic[num]=1
            else:
                dic[num]+=1
        heap=[]
        for key,val in dic.items():
            heapq.heappush(heap,(-val,key))
        ans=[]
        for i in range(k):
            tmp=heapq.heappop(heap)
            ans.append(tmp[1])
        return ans