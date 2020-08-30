class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k= k%n
        count=0
        start=0
        while (count!=n):
            cur=start
            pre=nums[cur]
            while (True):
                nt= (cur+k)%n
                tmp=nums[nt]
                nums[nt]=pre 
                pre=tmp
                cur=nt
                count +=1
                if (start==cur):
                    break
            start+=1