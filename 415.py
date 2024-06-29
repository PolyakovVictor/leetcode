class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        max_len = max(len(num1), len(num2))
        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)
        result = []
        carry = 0

        for i in range(max_len - 1, -1, -1):
            sum = int(num1[i]) + int(num2[i]) + carry
            carry = sum // 10
            result.append(str(sum % 10))
        if carry:
            result.append(str(carry))
        return "".join(result[::-1])


obj = Solution()

print(obj.addStrings(num1="11", num2="123"))
