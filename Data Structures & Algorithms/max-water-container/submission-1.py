class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        i, j = 0, len(heights)-1

        while i < j:
            shortest = heights[i]
            if heights[i] >= heights[j]:
                shortest = heights[j]
    
            width = j - i
            area = width * shortest
            if area > res:
                res = area

            if heights[i] < heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
                j -= 1
        return res