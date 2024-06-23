class Solution:
    def isHappy(self, n: int) -> bool:
        h = []
        while n != 1:
            n = sum(map(lambda x: pow(int(x), 2), str(n)))
            if n in h:
                return False
            h.append(n)
        return True


cls = Solution()

print(cls.isHappy(n=2))
