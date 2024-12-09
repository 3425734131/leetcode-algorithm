from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = 0
        max_value = -10**4-1
        for i in range(len(nums)):
            result += nums[i]
            max_value = max(max_value,result)
            result = max(0,result)
        return max_value
solution = Solution()
solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])