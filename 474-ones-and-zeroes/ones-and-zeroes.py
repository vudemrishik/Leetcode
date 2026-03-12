class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        mem = {}
        def zeros(s):
            cnt=0
            for i in s:
                if i=='0':
                    cnt += 1
            return cnt
        def ones(s):
            cnt=0
            for i in s:
                if i=='1':
                    cnt += 1
            return cnt
        def recurse(strs, m, n):
            if (m==0 and n==0) or len(strs)==0:
                return 0
            if (len(strs), m, n) in mem:
                return mem[(len(strs), m, n)]
            if m>=zeros(strs[0]) and n>=ones(strs[0]):
                ans = max(recurse(strs[1:], m, n), 1 + recurse(strs[1:], m-zeros(strs[0]), n-ones(strs[0])))
                mem[(len(strs), m, n)] = ans
                return ans
            else:
                ans = recurse(strs[1:], m, n)
                mem[(len(strs), m, n)] = ans
                return ans

        return recurse(strs, m, n)
            
        