# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         p1=0
#         while(nums[p1]!=0):
#                 p1+=1
#                 if (len(nums)==1 or p1==len(nums) ):
#                     return None
#         p2=p1+1  
#         while(p1<p2 and p1<len(nums) and p2<len(nums)):
#             while(p1<len(nums) and nums[p1]!=0):
#                 p1+=1
#             while(p2<len(nums) and nums[p2]==0):
#                 p2+=1
#             if(p1>p2 or p1>=len(nums) or p2>=len(nums)):
#                 break
#             nums[p1]=nums[p2]
#             nums[p2]=0
#             p1+=1
#             p2+=1     

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos=0
        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[pos],nums[i]= nums[i],nums[pos]
                pos+=1