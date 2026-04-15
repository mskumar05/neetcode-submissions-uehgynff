from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            ans = max(ans, width * h)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans