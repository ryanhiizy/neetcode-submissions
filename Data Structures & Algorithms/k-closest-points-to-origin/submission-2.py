import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        left = 0
        right = len(points) - 1
        target = k - 1

        while left <= right:
            i = left
            
            for j in range(left, right):
                x1, y1 = points[j]
                px, py = points[right]
                if math.sqrt((x1)**2 + (y1)**2) <= math.sqrt((px)**2 + (py)**2):
                    points[i], points[j] = points[j], points[i]
                    i += 1

            points[right], points[i] = points[i], points[right]
            
            if i == target:
                return points[:k]
            elif i <= target:
                left = i + 1
            else:
                right = i - 1