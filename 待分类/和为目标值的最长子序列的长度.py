from typing import List


class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [0] * len(nums)
        for i in range(len(nums)):



solution = Solution()
solution.lengthOfLongestSubsequence([1,2,3,4,5],9)