def hammingWeight(self, n: int) -> int:
        if not n: return 0
        count=0
        while(n!=0):
            count+=1
            n= n&(n-1)
        return count