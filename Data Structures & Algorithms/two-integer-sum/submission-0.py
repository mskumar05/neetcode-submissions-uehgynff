from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        
        for i in range(len(nums)):
            search = target - nums[i]
            if search in hashMap:
                return [hashMap[search], i]
            hashMap[nums[i]] = i
        
        return []  # fallback, though problem guarantees a solution exists