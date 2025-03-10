class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        dic = {}
        n = len(A)
        for i in range(1,n+1):
            dic[i] = 0
        for i in A:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] =1
        rep = 0 
        mis = 0      
        for i in dic.keys():
            if dic[i]==2 :
                rep = i
            if dic[i] ==0:
                mis = i 
                
        return [rep,mis]
                
        
        
""" a = Solution()
k = a.repeatedNumber([3,1,2,5,3])   
        
 """
 
k = (5*(5+1))//2
s = k *(2*5+1)//3

h = (5*(5+1)*(2*5+1))//6
print(h,s)
 