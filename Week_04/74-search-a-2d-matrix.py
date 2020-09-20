def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        m,n=len(matrix),len(matrix[0])
        left,right=0,m*n-1
        while(left<=right):
            mid=left+(right-left)//2
            mid_num=matrix[mid//n][mid%n]
            if(mid_num==target ): return True
            if(mid_num>target):
                right=mid-1
            else:
                left=mid+1
        return False