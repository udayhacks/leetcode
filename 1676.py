from re import S


class Solution:
    def maxOperations(self, nums, k: int) -> int:
        hash = {}
        for i in nums :
            if i in hash :
                hash[i] +=1
            else:
                hash[i]  = 1


        c = 0
        nums = set(nums)

        for i in nums :
            if k-i in hash and i in hash :
                if i == k-i :
                    c+=hash[i]//2
                    hash.pop(i)

                else:
                    c+=min(hash[i],hash[k-i])
                    hash.pop(k-i)
                    hash.pop(i)
                    
                    
        return c
                    
 
 

a = Solution()



k = 5
#k = 6
l = [3,1,3,3,3,4]

l = a.maxOperations(l,k)