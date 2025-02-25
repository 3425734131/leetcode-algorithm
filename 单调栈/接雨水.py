from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        result = 0
        for i, h in enumerate(height):
            if not stack or height[i] <= height[stack[-1]]:
                stack.append(i)
            else:
                while stack and height[i] > height[stack[-1]]:
                    current = stack.pop()
                    if not stack:
                        break
                    current_width = i - stack[-1] - 1
                    delta_height = min(height[i], height[stack[-1]]) - height[current]
                    result += delta_height * current_width
                stack.append(i)
        return result


s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
