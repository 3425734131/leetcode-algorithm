from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        border = 0
        current_right = 0
        ans = 0
        for i in range(n):
            current_right = max(current_right, i + nums[i])
            if current_right >= n - 1:
                return ans+1
            if i == border:
                border = current_right
                ans += 1
        return ans
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         length = len(nums)
#         if length == 1:
#             return 0
#         right = 1
#         dp = [0] * length
#         for i in range(length):
#             # 需要更新dp的最右边的停止位置
#             temp = nums[i] + i + 1
#             print(temp)
#             for j in range(right,min(temp,length)):
#                 dp[j] = dp[i] + 1
#             right = max(temp,right)
#             if right >= length:
#                 break
#         return dp[length-1]

soluntion = Solution()
print(soluntion.jump([2,3,1,1,4]))


