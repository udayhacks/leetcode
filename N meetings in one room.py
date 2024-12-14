#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        d =[]
        for i in range(len(start)):
            d.append([start[i],end[i]])
            
            
        d.sort(key = lambda x:x[1])   
        c = 1 
        endT=d[0][1]
        
        for i in range(1,len(start)):
            if d[i][0] > endT:
                c+=1
                endT=d[i][1]
        return c
                
            
        
        

a = Solution()
n = 6
start = [1,3,0,5,8,5]
end =  [2,4,6,7,9,9]          


l = a.maximumMeetings(n,start,end)
print(l)