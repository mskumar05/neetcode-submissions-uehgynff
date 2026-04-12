class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n  # will hold prefix products first

        # Left to right: store prefix products in res
        left = 1
        for i in range(n):
            res[i] = left
            left *= nums[i]

        # Right to left: multiply by suffix products
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res