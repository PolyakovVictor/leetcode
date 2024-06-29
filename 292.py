from typing import List


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 > 0


cls = Solution()

print(cls.canWinNim(n=9))
