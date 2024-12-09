from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right = nums[0]
        for i in range(len(nums)):
            if right < i:
                return False
            else:
                right = max(nums[i]+i,right)
        return True
