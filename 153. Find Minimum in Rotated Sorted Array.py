class Solution:
    def findMin(self, nums: List[int]) -> int:
        minVal = nums[0]

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= nums[0]:
                l = mid + 1
            elif nums[mid] < nums[0]:
                r = mid - 1
                minVal = min(minVal, nums[mid])

        return minVal
