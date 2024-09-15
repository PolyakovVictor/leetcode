from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dn = {}
        for i in nums:
            if i in dn:
                dn[i] += 1
            else:
                dn[i] = 1

        biggest = nums[0]
        for key in dn:
            if dn[key] >= dn[biggest] and dn[key] > len(nums) / 2:
                biggest = key

        return biggest


obj = Solution()
print(obj.majorityElement([6, 5, 5]))
