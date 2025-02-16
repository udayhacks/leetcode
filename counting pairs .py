class Solution:
    def countPairs(self, arr):
        from collections import deque
        ans = 0 
        d = {}
        for  i in range(len(arr)):
            if arr[i]  not in d :
               d[arr[i]] =deque()
            d[arr[i]].append(i)
             
             
             
        for i in range(len(arr)) :
            k = (9-arr[i])
            
            if k in d and len(d[k]) :
                j = 0 
                
                while j <len(d[k]):
                    if d[k][j] > i :
                        ans+=1
                        
                    else:
                        d[k].popleft()
                    j+=1
                    
            
                
            
                
        return ans
            
    
    
arr= [88 ,72 ,45 ,59 ,23 ,24 ,0 ,5 ,21, 68, 50, 51 ,29, 45, 13, 26, 0, 38, 2 ,23 ,100 ,45 ,39, 76, 13, 80 ,48 ,50 ,78, 16, 61, 73, 33, 5 ,65 ,85 ,15 ,17 ,24 ,96 ,77, 63 ,33 ,18 ,90 ,24 ,51 ,49 ,5 ,29 ,2 ,79 ,60 ,38 ,76 ,96, 33 ,32 ,4 ,54]
arr =[8,1,4,5]
arr = [3, 8, 8, 8, 7, 6, 8, 10, 3, 3]
sol = Solution()
k = sol.countPairs(arr)
print(k)