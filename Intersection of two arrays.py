



class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        #return: expected length of the intersection array.
        
        d ={}
        c = 0 
        
        for i in range(len(a)) : 
            
            d[a[i]]  = i 
            
            
            
        for i in range(len(b)) :
            
            
            if b[i]  in d :
                c +=1
        return c 
            



import sys 
sys.stdin = open("G:\leetcode\fileInput.txt","r")
sys.stdout = open ("o.txt","a")            



            
n , m = map(int, input().split())
l= list(map(int , input().split())) 
k = list(map(int , input().split())) 

a = Solution()

i = a.NumberofElementsInIntersection(l ,k,n,m )        
print(i)
        #code