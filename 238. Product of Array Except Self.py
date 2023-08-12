class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multiLeft = 1
        multiRight = 1
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = multiLeft
            multiLeft *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= multiRight
            multiRight *= nums[i]

        return res
