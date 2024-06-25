class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        import heapq 
        heapq.heapify(nums)
        i = 0 
        h= sys.maxsize 
        j = len(nums)-1
        while i < j:
            h = min((nums[i]+nums[j])//2,h)
            i+=1
            j-=1
            
        return h