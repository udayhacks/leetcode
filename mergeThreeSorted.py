class Solution:
    #User function Template for python3
    #Function to merge three sorted arrays into a single array.
    def mergeThree(self, A,B,C):
        #code here
        def help(a,b):
            l = []
            i = 0 
            j = 0
            while j < len(b) and i < len(a ):
                if a[i] < b[j] :
                    l.append(a[i])
                    i+=1
                    
                elif a[i] > b[j]:
                    l.append(b[j])
                    j+=1
                    
                elif a[i]== b[j] :
                    
                    l.append(a[i])
                    l.append(b[j])
                    j+=1
                    i+=1  
                    
                    
            while i < len(a):
                l.append(a[i])
                i+=1
            while j < len(b) :
                l.append(b[j])
                j+=1   
            return l
        k = help(A,B)
        return help(k,C)
                
                
                
                
a =  Solution()


A= [1, 2, 3, 4] 
B= [1 ,2 ,3 ,4 ,5] 
C= [1 ,2, 3, 4, 5, 6]
a.mergeThree(A,B,C) 