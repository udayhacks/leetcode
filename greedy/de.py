class Solution:
    def maxI(self,i,j,arr): 
        
        max = -1
        index = 0
        for k in range(i,j) :
            if arr[k] > max :
                max = arr[k]
                index = k
        return index
    
    def minJumps(self, arr):
        n = len(arr)
        if n ==0 :
            return 0
        if arr[0] == 0 :
            return -1
        i = 1
        c = 1
        
        for i in range(n):
            
            if arr[i] >= (n-1-i):
                return c+1
            else:
                i = self.maxI(i+1,i+arr[i],arr)
                c+=1
                
        return c
    
    
    
    
    
a = Solution()
k = a.minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9] )
print(k)            
                
                
                
            
    	  
       
	            
	            
	  