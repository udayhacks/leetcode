#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):  
        
        
        
        
        
    
        
        a = {}

        b = {}
        
        
        for i in A:
            if i in a :
                a[i] +=1
            else: 
                a[i]  = 1  
                
        for i in B:
            if i in b :
                b[i] +=1 
                
            else :
                b[i]  = 1 
                
                
                
        
        
        for i in A :
            if i not in b :
                return False 
            if i in  b and a[i] != b[i] :
                return False 
                 
        
        
        
        
   
              
              
                
        return True 
                
        
        
        



a= Solution()
a.check([1,2,3,4,5],[5,4,3,2,1],5)