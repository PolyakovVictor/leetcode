class Solution:
    def __init__(self):
        self.memo = {}

    def climbStairs(self, n: int) -> int:
        print(self.memo)
        if n in self.memo:
            return self.memo[n]
        if n == 0 or n == 1:
            return 1
        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]


cls = Solution()
print(cls.climbStairs(n=44))
