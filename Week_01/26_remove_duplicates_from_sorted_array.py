class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        last_pos=0
        count=1
        for i in range(len(nums)):
            if(nums[i]!=nums[last_pos]):
                nums[last_pos+1]=nums[i]
                last_pos+=1
                count+=1
        return count