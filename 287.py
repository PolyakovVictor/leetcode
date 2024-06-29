from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        bit_sum = 0
        for i in range(0, len(nums)):
            bit_sum ^= nums[i]
            print(bit_sum, nums[i])
        return bit_sum


obj = Solution()

print(obj.findDuplicate(nums=[3, 1, 3, 4, 2]))
