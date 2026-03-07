class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total = 0
        f = 0
        total = sum(nums)
        f = sum([i*nums[i] for i in range(len(nums))])
        res = f
        for i in range(1, len(nums)):
            f += total - (len(nums))*nums[len(nums)-i]
            res = max(res, f)
        return res
