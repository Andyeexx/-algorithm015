class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for idx, num in enumerate(nums):
            hashmap[num]=idx
        for idx, num in enumerate(nums):
            if(hashmap.get(target-num) and hashmap[target-num]!=idx):
                return [idx,hashmap[target-num]]
        return None