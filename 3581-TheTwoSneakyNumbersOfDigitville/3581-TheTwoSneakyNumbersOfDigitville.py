# Last updated: 04/04/2026, 13:10:42
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()
        for i in range(1,len(nums)) :
            if nums[i-1] == nums[i] :
                ans.append(nums[i])

        return ans


        