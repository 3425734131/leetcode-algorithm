from typing import List


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = dict.get(nums[i],0) + 1
        maxnum = 0
        arr = []
        for key,value in dict.items():
            maxnum = max(maxnum,value)
            arr.append(value)
        result = 2*maxnum - sum(arr)
        if result >= 0:
            return result
        else:
            return abs(result)%2

solution = Solution()
solution.minLengthAfterRemovals([2,3,4,4,4])