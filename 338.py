from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        for i in range(1, n + 1):
            print(
                (3 << 4) >> 4,
                result,
                bin(3),
                bin(48),
                result[i >> 1] + (i & 1),
                result[i >> 1],
                (i & 1),
            )
            result[i] = result[i >> 1] + (i & 1)
        return result


cls = Solution()
print(cls.countBits(n=200))
