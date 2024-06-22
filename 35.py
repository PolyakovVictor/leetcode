from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            print(low, high, mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                print("less")
                low = mid + 1
                print("low", low)
            else:
                high = mid - 1
        return mid


if __name__ == "__main__":
    obj = Solution()
    result = obj.searchInsert(nums=[1, 3, 5, 6], target=2)
    print(result)
