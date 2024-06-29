from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        out = 0
        for x in nums:
            out ^= x
            print(out)
        return out


cls = Solution()

print(cls.singleNumber(nums=[4, 1, 2, 1, 2]))
