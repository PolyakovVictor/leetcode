class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        result = []
        for i in range(left, right):
            for j in str(i):
                result.append([j for j in str(i) if int(j) != 0 and i % int(j) == 0])

        return result


obj = Solution()
print(obj.selfDividingNumbers(1, 22))
