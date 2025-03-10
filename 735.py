

class Solution1:
    def asteroidCollision(self, asteroids):
        stack = []
        for i in asteroids:
            if i <0 :
                sign = False
            if i > 0 :
                sign = True
            if not stack :
                stack.append([i,sign])  
      
            else :
                if (stack[-1][1] == True and sign == True) or (stack[-1][1] == False and sign == False): 
                    stack.append([i,sign]) 
                else :
                    while stack and stack[-1][1] != sign:
                        if abs(stack[-1][0]) == abs(i):
                            stack.pop()
                            break
                        elif abs(stack[-1][0]) > abs(i):
                            break
                        elif abs(stack[-1][0]) < abs(i):
                            stack.pop()
                            if not stack :
                                stack.append([i,sign]) 
                                break
                    
        ans = []      
        for i in range(len(stack)): 
                ans.append(stack[i][0])
                
                
                    
                   


        return ans 

        
        
a = Solution1()
print(a.asteroidCollision([-2,-1,1,2]))


class Solution:
    def asteroidCollision(self, asteroids):
        res = []

        for a in asteroids:
            while res and a < 0 < res[-1]:
                if -a > res[-1]:  # Current asteroid wins
                    res.pop()
                    continue
                elif -a == res[-1]:  # Both explode
                    res.pop()
                break
            else:  # No collision
                res.append(a)

        return res



a2 = Solution()
print(a.asteroidCollision([4,7,1,1,2,-3,-7,17,15,-16]))
