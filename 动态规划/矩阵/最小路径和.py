from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = grid[rows-1]
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i == rows - 1 and j == cols - 1:
                    continue
                elif i == rows - 1:
                    dp[j] += dp[j+1]
                elif j == cols - 1:
                    dp[j] += grid[i][j]
                else:
                    dp[j] = min(dp[j],dp[j+1])+grid[i][j]
        return dp[0]

solution = Solution()
print(solution.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))

