from typing import List


# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         num = len(s)
#         dp = [[-1] * num for _ in range(num)]
#         temp = 0
#         dp[0][0] = 1
#         dp[num-1][num-1] = 1
#         for i in range(num):
#             # 奇数回文子序列
#             temp = max(temp,self.work(i,i,s,dp)*2 -1)
#             if i != num-1:
#                 # 偶数回文子序列
#                 temp = max(temp,self.work(i,i+1,s,dp)*2)
#         print(dp)
#         return temp
#
#     def work(self,left:int,right:int,s:str,dp:List[List[int]]) ->int:
#         if left < 0 or right >= len(s):
#             return 0
#         if dp[left][right] != -1:
#             return dp[left][right]
#         if s[left] == s[right]:
#             dp[left][right] = self.work(left-1,right+1,s,dp)+1
#         else:
#             dp[left][right] = max(self.work(left,right+1,s,dp),self.work(left-1,right,s,dp))
#
#         return dp[left][right]

# 上面递归式实现动态规划 容易栈溢出

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        num = len(s)
        dp = [[0] * num for _ in range(num)]

        # 每个字符本身就是回文子序列，初始化 DP 表
        for i in range(num):
            dp[i][i] = 1

        # 填充 DP 表
        for length in range(1, num):  # 判断长度为2到num-1的子串中最长回文序列
            for left in range(num - length):
                right = left + length
                if s[left] == s[right]:
                    dp[left][right] = dp[left + 1][right - 1] + 2
                else:
                    dp[left][right] = max(dp[left + 1][right], dp[left][right - 1])

        return dp[0][num - 1]


solution = Solution()
print(solution.longestPalindromeSubseq("bbbab"))
