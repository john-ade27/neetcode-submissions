class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if 1 <= len(nums) <= 100000:
            i = 0
            max_consecutive = 0
            consecutive = 0

            while i < len(nums):
                if nums[i] == 1:
                    consecutive += 1
                else:
                    consecutive = 0

                if max_consecutive <= consecutive: 
                    max_consecutive = consecutive
  
                i += 1
            return max_consecutive

        else:
            return False