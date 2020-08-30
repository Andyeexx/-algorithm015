class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        ans=0
        n=len(height)
        left=0
        right=n-1
        max_left=height[0]
        max_right=height[right]
        while(left<=right):
            max_left=max(max_left,height[left])
            max_right=max(max_right,height[right])
            if(max_left<max_right):
                ans+=max_left-height[left]
                left+=1
            else:
                ans+=max_right-height[right]
                right-=1
        return ans