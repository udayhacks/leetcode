class Solution:
    
    def insert(self, intervals, newIntervals) :
        ans = []
        if len(intervals)==0 :
            return [newIntervals]
        if len(intervals)==1 :
            if newIntervals[0] < intervals[0][0] :
                ans.append(newIntervals)
                newIntervals= intervals[0]
            else:
                ans.append(intervals[0])
            if ans[-1][0] <= newIntervals[0] and ans[-1][1] >= newIntervals[0]   :
                    k = [min(ans[-1][0],newIntervals[0]), max( ans[-1][1],newIntervals[1] )     ]
                    ans[-1] = k 
            else:
                    ans.append(newIntervals)     
                    
            return ans            
        
        for i in range(len(intervals)):
            if intervals[i][0] > newIntervals[0]:
                intervals.insert(i, newIntervals)
                ans.append(intervals[0]) 
                break
        if len(ans) == 0 :
            ans.append(intervals[0]) 
            intervals.append(newIntervals)
            
        for i in range(1,len(intervals)):
            if ans[-1][0]<= intervals[i][0] and ans[-1][1] >= intervals[i][0] :
                k = [min(ans[-1][0],intervals[i][0]), max( ans[-1][1],intervals[i][1] )     ]
                ans[-1] = k 
            else:
                ans.append(intervals[i])
        return ans 
            

a = Solution()
l = a.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8])
print(l)
print([[1,2],[3,10],[12,16]])

l=a.insert([[0,1]],[1,2])
print(l)

l = a.insert([[1,5]],[0,3])
print(l)


l = a.insert([[2,6],[7,9]],[15,18])
print(l)
