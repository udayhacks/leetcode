from re import S


class Solution:
    def rotate(self, nums,k):
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k%l 
        nums[l-k:], nums[:l-k] = nums[:l-k],nums[l-k:]
        
        
a = Solution()
a.rotate(
[3,1, 6, 5, 10 ,7 ,6 ,6 ,1 ,7]
 
)