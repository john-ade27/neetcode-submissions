class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        k = 0
        while i < len(nums):
            if val != nums[i]:
                nums[k] = nums[i]
                k += 1
            i += 1
        return k
