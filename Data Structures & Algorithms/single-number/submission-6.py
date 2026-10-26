class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for num in nums:
            count = 0
            for i in range(len(nums)):
                if num ^ nums[i] == 0:
                    count += 1
            if count < 2: return num
