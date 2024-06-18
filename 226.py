class Solution:
    def majorityElement(self, nums):
        e1 = -float("inf")
        e2 = -float("inf")

        c1 = c2 = 0 
        
        for i in nums:
            
            if c1 == 0 and i != e2 :
                e1 = i 
                c1 = 0 

            elif c2 == 0 and i != e1 :
                e2 = i 
                c2 = 1

            elif i == e1 : c1+=1
            elif i == e2 : c2+=1
            else:
                c1-=1
                c2-=1


        

        m = int(len(nums)/3)+1

        c1 = c2 = 0 

        for i in nums :
            if e1 == i :
                c1 +=1 
            elif e2 ==i :
                c2 +=1
        ans = []
        if c1 >= m :
            ans.append(e1)
        if c2 >= m :
            ans.append(e2) 


        return ans
    
    
    
a= Solution()
nums = [3,3,4]
a.majorityElement(nums)