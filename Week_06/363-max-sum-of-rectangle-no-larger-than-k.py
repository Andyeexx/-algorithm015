def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix: return 0
        ans,row,col= -float('inf'),len(matrix),len(matrix[0])
        for l in range(col):
            row_sum=[0]*row
            for r in range(l,col):
                for i in range(row):
                    row_sum[i]+=matrix[i][r]
                lst=[0]
                summ=0
                for num in row_sum:    
                    summ+=num
                    loc = bisect.bisect_left(lst,summ-k)
                    if(loc < len(lst) and summ-lst[loc]>ans): ans=summ-lst[loc]
                    bisect.insort(lst,summ)
        return ans