class Solution:
    def divideArray(self, nums):
       hash = {}
       n = len(nums)
       k = n//2
       for i in nums:
           if i not in hash:
               hash[i] =1
           else:
               hash[i]+=1
       if len(hash)  != k :
           return False
       check = 0 
       
       for  i , j in hash.items():
        
           
       if check :
            return False
       return True
           
           
        

a = Solution()
arrK = [3,2,3,2,2,2]
a.divideArray(arrK)