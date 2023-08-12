class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        nums.sort()
        maxNum = 1
        currNum = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                currNum += 1
                maxNum = max(maxNum, currNum)
            elif nums[i] == nums[i - 1]:
                continue
            else:
                currNum = 1

        return maxNum
