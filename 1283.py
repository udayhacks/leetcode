"""_summary_

Given an array of integers nums and an integer threshold, we will choose a positive integer divisor,
divide all the array by it, and sum the division's result. Find the smallest divisor 
such that the result mentioned above is less than or equal to threshold.
Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).
The test cases are generated so that there will be an answer.




"""





class Solution:
    
    def check (self, nums,thresold,mid):
        res = 0 
        from math import ceil
        for i in nums :
            res+=ceil(i/mid)
        return res <= thresold
    
    def smallestDivisor(self, nums, threshold: int) -> int:
        
        mx = nums[0]
        for i in nums :
            mx = max(mx,i)
            
        mn = 1  
        while mn <= mx :
            mid = (mn+mx)//2
            if self.check(nums,threshold,mid) :
                mx = mid-1
            else:
                mn = mid+1        
        return mn
                
                
                
                
a = Solution()
a.smallestDivisor([44,22,33,11,1],5)