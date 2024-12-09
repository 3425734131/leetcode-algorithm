from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [0] * cols
        dp[cols - 1] = 1
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                    continue
                if i == rows - 1 and j == cols - 1 or j == cols - 1:
                    continue
                elif i == rows - 1:
                    dp[j] = dp[j + 1]
                else:
                    dp[j] += dp[j + 1]
        return dp[0]


solution = Solution()
print(solution.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
