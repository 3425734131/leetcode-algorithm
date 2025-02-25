from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = 0
        min_value = 1000000001
        for i in range(len(nums)):
            left , right = i+1 ,len(nums)-1
            current_min_value = 1000000001
            current_result = 0
            while left < right:
                t = nums[i] + nums[left] + nums[right]
                if t < target:
                    left += 1
                elif t == target:
                    return target
                else:
                    right -= 1
                if abs(target - t) < current_min_value:
                    current_min_value = abs(target -t)
                    current_result = t
            if current_min_value < min_value:
                min_value = current_min_value
                result = current_result
        return result

solution  = Solution()
print(solution.threeSumClosest([0,0,0],1))

