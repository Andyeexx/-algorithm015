def search(self, nums: List[int], target: int) -> int:
        if(not nums):return -1
        left,right=0,len(nums)-1
        while(left<=right):
            mid=left+(right-left+1)//2
            if(nums[mid]==target):
                return mid
            if(nums[mid]> nums[0]): #左递增
                if (target<nums[mid] and target>=nums[0]):
                    right=mid-1
                else:
                    left=mid+1
            else:
                if(target>nums[mid] and target<=nums[-1]):
                    left=mid+1
                else:
                    right=mid-1
        return -1