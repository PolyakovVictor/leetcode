from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        triangle = [[1]]

        for i in range(1, rowIndex + 1):
            row = [1]
            prev_row = triangle[i - 1]

            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])

            row.append(1)
            triangle.append(row)
        print(triangle)
        return triangle[rowIndex]


cls = Solution()
print(cls.getRow(3))
