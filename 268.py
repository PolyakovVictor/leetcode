from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nl = len(nums)
        r = sum(nums)
        er = sum(range(1, nl + 1))
        return er - r


cls = Solution()

print(cls.missingNumber(nums=[0, 1]))
