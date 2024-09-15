from functools import reduce


class Solution:
    def hammingWeight(self, n: int) -> int:
        print(bin(n)[2:])
        return reduce(lambda a, b: a + (1 if b == "1" else 0), bin(n)[2:], 0)


obj = Solution()
print(obj.hammingWeight(11))
