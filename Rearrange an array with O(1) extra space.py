#User function Template for python3

##Complete this code

class Solution:
    #Function to rearrange an array so that arr[i] becomes arr[arr[i]]
    #with O(1) extra space.
    def arrange(self,arr, n): 
        #Your code here
        for i in range(n):
            k = arr[i]+(arr[arr[i]]%n)*n
            arr[i]=k

        for i in range(n):
            arr[i] //=n
            
            
            
a= Solution()
l =[4,0,2,1,3]
a.arrange(l,len(l))

        
        
        #Your code here
