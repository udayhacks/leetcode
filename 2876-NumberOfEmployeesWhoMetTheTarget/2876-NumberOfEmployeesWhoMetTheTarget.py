# Last updated: 04/04/2026, 13:11:27
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0 
        for i in range(len(hours)):
            if hours[i] >=target :
                count +=1
        return count 
                
        