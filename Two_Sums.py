class Solution(object):
    def twoSum(self, nums, target):
        nums_seen = {}
        for i, num in enumerate(nums):
            complement = target - num
        
            if complement in nums_seen:
               return [nums_seen[complement], i]
            
            nums_seen[num] = i
        
        return[]
