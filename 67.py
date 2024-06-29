class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))

        a = a.zfill(max_len)
        b = b.zfill(max_len)

        carry = 0
        result = []

        for i in range(max_len - 1, -1, -1):
            sum = int(a[i]) + int(b[i]) + carry
            carry = sum // 2
            result.append(str(sum % 2))

        if carry:
            result.append("1")

        return "".join(result[::-1])


cls = Solution()
print(cls.addBinary(a="11", b="1"))
