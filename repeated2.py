#User function Template for python3

class Solution:
    
    #Function to find two repeated elements.
    def twoRepeated(self, arr , N):
        
        
        d = dict()
        a = 0 
        b = 0
        l = []
        
        for i in arr :
            if i in d :
                d[i]+=1 
                
            if i not in d :
                d[i] = 1
            if d[i] == 2 :
                l.append(i)
                
           
        return  l
        #Your code here
        
        
        
a = Solution()
a.twoRepeated([1, 2, 1, 3, 4 ,3],4)