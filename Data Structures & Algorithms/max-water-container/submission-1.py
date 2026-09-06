class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        area = 0
        l, r = 0 , len(heights) - 1

        while l < r:
            width = r - l
            curArea = min(heights[l],heights[r]) * width
            area = max(area, curArea)
            
            if heights[l] > heights[r]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1
            else:
                l += 1

        
        return area

