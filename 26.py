from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        k = 0
        for i in range(len(nums)):
            if nums[i] != prev:
                prev = nums[i]
                nums[k] = nums[i]
                k += 1
        nums = nums[:k]
        print(nums)
        return k


obj = Solution()
print(obj.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
