class Solution:
    def tribonacci(self, n: int) -> int:
        seq = [0, 1, 1]
        for i in range(2, n):
            seq.append(seq[i] + seq[i - 1] + seq[i - 2])
        return seq[n]


obj = Solution()
print(obj.tribonacci(n=10))
