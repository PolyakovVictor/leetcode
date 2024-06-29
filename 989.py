from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num_len = len(num)
        k = str(k)
        k_len = len(k)

        if num_len < k_len:
            num = [0] * (k_len - num_len) + num
        else:
            k = k.zfill(num_len)
        k = [int(i) for i in k]
        result = []
        carry = 0
        max_len = max(len(k), len(num))

        for i in range(max_len - 1, -1, -1):
            sum = num[i] + k[i] + carry
            carry = sum // 10
            result.append(sum % 10)
        if carry:
            result.append(carry)
        return result[::-1]


obj = Solution()

print(obj.addToArrayForm(num=[0], k=23))
