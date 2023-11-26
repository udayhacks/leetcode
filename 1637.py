class Solution:
    def maxWidthOfVerticalArea(self, points) -> int: 
        k = lambda x :x[1]
        points.sort(key = k )
        return points
        
        
        
        
        
a = Solution()
points = [[8,7],[9,9],[7,4],[9,7]]
points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]

points =a.maxWidthOfVerticalArea(points) 


print(points)
        