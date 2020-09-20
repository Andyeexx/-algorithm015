def findMin(self, nums: List[int]) -> int:
        if not nums: return None
        left,right= 0,len(nums)-1
        mini=float('inf')
        while (left<=right):
            mid=(left+(right-left)//2)
            mid_num=nums[mid]
            if(mid_num>=nums[0]):
                mini=min(mini,nums[left],mid_num)
                left=mid+1
            else:
                mini=min(mini,nums[right],mid_num)
                right=mid-1
        return mini