class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        l=len(nums)
        total = sum(nums)
        f = sum([i*nums[i] for i in range(l)])
        res = f
        for i in range(1, l):
            f += total - (l)*nums[l-i]
            res = max(res, f)
        return res
