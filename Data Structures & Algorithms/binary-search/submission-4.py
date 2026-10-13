class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        n = len(nums) - 1

        while l <= n:
            mid = (l+n) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                n = mid - 1
            else:
                return mid
        return -1