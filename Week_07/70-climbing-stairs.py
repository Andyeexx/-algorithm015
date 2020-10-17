def climbStairs(self, n: int) -> int:
    if n<3: return n
    pre,cur=1,2
    for i in range(2,n):
        pre,cur=cur,pre+cur
    return cur