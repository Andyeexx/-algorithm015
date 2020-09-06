class Solution:
    def nthUglyNumber(self, n: int) -> int:        
        heap=[]
        heapq.heappush(heap,1)
        ugly=[]
        seen=[]
        count=0
        times=[2,3,5]
        while(count!=n):
            min_num=heapq.heappop(heap)
            ugly.append(min_num)
            count+=1
            for time in times:
                if(time*min_num not in seen):
                    heapq.heappush(heap,time*min_num)
                    seen.append(time*min_num)
        return ugly[-1]