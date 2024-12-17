from collections import Counter
from typing import List
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans = left = 0
        cnt = Counter()
        for key, value in enumerate(nums):
            cnt[value] += 1
            while max(cnt) - min(cnt) > 2:
                y = nums[left]
                cnt[y] -= 1
                if cnt[y] == 0:
                    del cnt[y]
                left += 1
            ans += key - left + 1
        return ans

solution = Solution()
solution.continuousSubarrays([65,66,67,66,66,65,64,65,65,64])

