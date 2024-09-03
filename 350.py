from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1:
            return []

        result = []
        for i in nums1:
            if i in nums2:
                result.append(i)
                nums2[nums2.index(i)] = ""
            print(i, nums1, nums2, result)

        return result


o = Solution()
print(o.intersect(nums1=[1, 2], nums2=[1, 1]))
