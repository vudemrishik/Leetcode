class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        mem = [-1 for i in range(target+1)]
        def recurse(t):
            if t==0:
                return 1
            elif t<0:
                return 0
            if mem[t]!=-1:
                return mem[t]
            else:
                res = 0
                for i in range(len(nums)):
                    res += recurse(t-nums[i])
                mem[t] = res
                return res

        return recurse(target)

            