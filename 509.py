class Solution:
    def fib(self, n: int) -> int:
        seq = [0, 1]
        for i in range(1, n):
            seq.append(seq[i] + seq[i - 1])

            print(seq[i] + seq[i - 1], seq)
        return seq[n]


obj = Solution()
print(obj.fib(3))
