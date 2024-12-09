from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        for i in range(1,rows,1):
            for j in range(len(triangle[i])):
                if i == j:
                    triangle[i][j] += triangle[i-1][j-1]
                    continue
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                    continue
                triangle[i][j] += min(triangle[i-1][j-1],triangle[i-1][j])
        temp = triangle[rows-1][0]
        for j in range(rows):
            temp = min(temp,triangle[rows-1][j])
        return temp




solution = Solution()
print(solution.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))