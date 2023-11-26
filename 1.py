class Solution:
    def twoSum(self, nums, target: int) :
        note = {}

        for i in range(len(nums)) :

            d = target - nums[i] 
            if d in note :
                return [note[d], i ]

            note[nums[i]] = i  
            
            
            
a = Solution ()
nums = [2,7,11,15]
target = 9
a.twoSum(nums,target)   
    