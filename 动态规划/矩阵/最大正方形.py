from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        columns = len(matrix[0])
        result = 0
        dp = [[0] * columns for _ in range(rows)]
        for i in range(columns):
            if matrix[0][i] == "1":
                dp[0][i] = 1
                result = 1
        for i in range(rows):
            if matrix[i][0] == "1":
                dp[i][0] = 1
                result = 1
        for i in range(1,rows,1):
            for j in range(1,columns,1):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1]) + 1
                    result = max(result, dp[i][j])
        return result * result
solution = Solution()
print(solution.maximalSquare([["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]]))