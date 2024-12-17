from typing import List
import bisect

# 区间重叠最大数（线段）
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        num = 0
        for i in range(len(nums)):
            left = bisect.bisect_right(nums, nums[i]+2*k)
            num = max(num,left - i)

solution = Solution()
solution.maximumBeauty([4,6,1,2], 2)


