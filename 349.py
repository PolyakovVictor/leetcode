from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1:
            return []

        result = []

        for i in nums1:
            if i in nums2 and i not in result:
                result.append(i)

        return result


obj = Solution()
print(obj.intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]))
