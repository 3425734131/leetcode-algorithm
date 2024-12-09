class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        rows = len(s2)
        columns = len(s1)
        dp = [[0]*(columns+1) for _ in range(rows+1)]

        for i in range(1,columns+1,1):
            dp[0][i] = dp[0][i-1]+ord(s1[i-1])
        for j in range(1,rows + 1,1):
            dp[j][0] = dp[j-1][0]+ord(s2[j-1])

        for i in range(1,rows+1,1):
            for j in range(1,columns+1,1):
                if s1[j-1] == s2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j - 1] + ord(s1[j -1]),dp[i-1][j] + ord(s2[i-1]))
        return dp[rows][columns]


solution = Solution()
solution.minimumDeleteSum("sea","eat")