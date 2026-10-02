class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1]*(n+1)
        def help(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = help(i+1)+help(i+2)
            return cache[i]
        return help(0)
            