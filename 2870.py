class Solution:
    def minOperations(self, nums) -> int:
        import math
        
        hash = {}
        
        for i in nums :
            if i in hash :
                hash[i] +=1
            else:
                hash[i] = 1 
                
        c = 0        
                
        for i in hash :
            if (hash[i] % 3 == 0 or hash[i] %3 == 2) or hash[i] % 2 == 0 :
                 
                 #pass
                
                a = 10**6
                b = 10**6
                
                
                if hash[i] % 3 == 0 or hash[i] %3 == 2 :
                    a = math.ceil(hash[i]/3)
                elif hash[i] % 2== 0 :
                    b = math.ceil(hash[i]/2)
                    
                c+= min(a,b)
                
            else:
                return -1
            
        return c
                    
                            
                
        
        
    
        

from collections import Counter

class Solution:
    def minOperations(self, nums) -> int:
        counts = Counter(nums)
        count = 0

        for frequency in counts.values():
            if frequency == 1:
                return -1

            remainder = frequency % 3
            if remainder == 0:
                count += frequency // 3
            else:
                count += frequency // 3 + 1

        return count     
        
        
        
        
        
        
        
        
        
        
        
        
a = Solution()
nums = [2,3,3,2,2,4,2,3,4] 
nums = [2,1,2,2,3,3]
nums = [14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12] 
a.minOperations(nums)     