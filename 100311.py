class Solution:
    def countDays(self, days: int, meetings):
        
        
        
        
        meetings.sort()
        temp= [meetings[0]]
        
        for i in range(1,len(meetings)) :
            if temp[-1][1] >= meetings[i][0] :
                temp[-1][1] = max(meetings[i][1],temp[-1][1])
                
            else:
                temp.append(meetings[i])
        ans = 0 
        for i in temp :
            ans +=(( i[1]-i[0])+1) 
            
            
        return days-ans



a = Solution()
days = 14 
meetings = [[6,11],[7,13],[8,9],[5,8],[3,13],[11,13],[1,3],[5,10],[8,13],[3,9]]
a.countDays(days,meetings)
                