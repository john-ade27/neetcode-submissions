class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        k = 0
        consecutive = 0 
        while i < len(nums):
            if nums[i]== 1:
                k += 1
            else:
                k = 0

            if consecutive <= k:
                consecutive = k
            i += 1
        return consecutive
                
