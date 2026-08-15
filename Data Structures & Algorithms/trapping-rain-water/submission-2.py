class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        res = 0

        max_left = 0
        for i in range(len(height)):
            prefix[i] = max_left
            max_left = max(max_left, height[i])
            
        max_right = 0
        for i in range(len(height) - 1, -1, -1):
            suffix[i] = max_right
            max_right = max(max_right, height[i])

        for i in range(len(height)):
            curr = min(prefix[i], suffix[i]) - height[i]
            if curr > 0:
                res += curr

        return res