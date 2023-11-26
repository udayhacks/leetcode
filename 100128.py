class Solution:
    def findHighAccessEmployees(self, access_times):
        access_times.sort(key = lambda x :x[0])
        access_times.sort(key = lambda x :x[1])
        ans = dict()
        for i in range(1,len(access_times)):
            if access_times[i][0] == access_times[i-1][0] :
                            
                        if (int(access_times[i][1]) -int(access_times[i-1][1])) <100 :
                            if access_times[i][0] in ans :
                                ans[(access_times[i][0])]+=1
                            else:
                                ans[(access_times[i][0])]= 1 
                                
                                
                                
        res = []             
        for i in ans.keys() :
                    if ans[i] >= 3 :
                        res.append(i)
                    
                                
                                
        
                                
                            
                            
        return res
    
    
    
    
    
a= Solution()
a.findHighAccessEmployees( [["a","0549"],["b","0457"],["a","0532"],["a","0621"],["b","0540"]])