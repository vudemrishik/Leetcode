class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        total = 0
        l = len(nums)
        for i in range(l):
            total += nums[i]
        mem = {}
        def recurse(i, j, s):
            if i==j:
                return nums[i]
            if i==j-1:
                return max(nums[i], nums[j])
            if (i, j) in mem:
                return mem[(i, j)]
            res1 = 0
            opp1 = recurse(i+1, j, s-nums[i])
            res1 += s-opp1
            res2 = 0
            opp2 = recurse(i, j-1, s-nums[j])
            res2 += s-opp2
            res = max(res1, res2)
            mem[(i, j)] = res
            return res

        res = recurse(0, l-1, total)
        print(res)
        return total-res <= res