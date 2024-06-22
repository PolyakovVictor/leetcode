from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return list(set(nums))


obj = Solution()
print(obj.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
