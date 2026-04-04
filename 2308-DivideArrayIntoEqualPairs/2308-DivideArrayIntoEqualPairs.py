# Last updated: 04/04/2026, 13:12:04
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        for count in counter.values():
            if count % 2 != 0:
                return False
        
        return True