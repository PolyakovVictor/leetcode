class Solution:
    def integerBreak(self, n: int) -> int:
        result = []

        def backtrack(remaining, combination, start):
            if remaining == 0:
                result.append(list(combination))
                return
            for i in range(start, n + 1):
                if i > remaining:
                    break
                combination.append(i)
                backtrack(remaining - i, combination, i)
                combination.pop()

        backtrack(n, [], 1)
        for i in range(len(result)):
            if len(result[i]) >= 2:
                max_num = 1
                for j in result[i]:
                    max_num *= j
                result[i] = max_num
            else:
                result.remove(result[i])
        return max(result)


obj = Solution()
print(obj.integerBreak(n=2))
