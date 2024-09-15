from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            dgt = target - v
            if dgt in nums and nums.index(dgt) != i:
                return [i, nums.index(dgt)]
        return []


obj = Solution()

result = obj.twoSum([3, 2, 4], target=6)

print(result)
