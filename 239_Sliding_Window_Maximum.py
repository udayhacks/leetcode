""" 
for not duplicate elements 

class Solution:
    def maxSlidingWindow(self, nums, k):
        
        start = 0 
        a = float('-inf')
        ans = []
        b = 0 
        for  end in range(len(nums)):
            if a< nums[end]:
                b = a
                a = nums[end]
            if nums[end] <a and b<nums[end] :
                b = nums[end]
            
            
            
            if end - start + 1 == k:
                ans.append(a)
                if a == nums[start]:
                    a = b
                    
                start+=1
        return ans 
            
            



class Solution:
    def maxSlidingWindow(self, nums, k):
        
        start = 0 
        a = [float('-inf'),-1]
        ans = []
        b = [float('-inf'),-1]
        for  end in range(len(nums)):
            if a[0]< nums[end]:
                b = a[:]
                a[0] = nums[end]
                a[1]= end 
            if nums[end] <=a[0] and b[0]<nums[end] and a[1] < end  :
                b[0] = nums[end]
                b[1] = end















 """






from collections import deque
from heapq import heapify
class Solution:
    def maxSlidingWindow(self, nums, k):
        ans = []
        kk = []
        start = 0 
        for i in range(len(nums)):
            if i -start == k :
                j = kk.pop[start]
                heapify(kk)
                m = max(-nums[i],-j)
                ans.append(m)
                
            else:
                kk.append(-nums[i])

        return ans 
            
a = Solution()
print(a.maxSlidingWindow([3,1,-1,-3,5,3,6,7],3))
print(a.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
print(a.maxSlidingWindow([1,3,4,-3,5,3,6,7],3))
print(a.maxSlidingWindow([-7,-8,7,5,7,1,6,0],4))
print(a.maxSlidingWindow([10,9,8,7,6,5,4,3,2,1],5))

#print([3,1,-1,-3,5,3,6,7])