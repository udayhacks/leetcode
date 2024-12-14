#User function Template for python3

from re import T


class Job:
    
    # Job class which stores profit and deadline.
    
    def __init__(self,id=0,deadline=0,profit=0):
        self.profit = profit
        self.deadline = deadline
        self.id = id
    
    
    
    
    
    
    
    
Jobs = [(1,4,20),(2,1,10),(3,1,40),(4,1,30)]
Jobs = [[1 ,2 ,100] ,[2 ,1 ,19] ,[3 ,2 ,27], [4 ,1 ,25] ,[5 ,1 ,15]]
l = []


for i in Jobs:
    sn,d,p = i
    l.append(Job(sn,d,p))
    
    
    
print(l)
    
"""    
l.sort(key = lambda x:(x.deadline,x.profit),reverse=True)


for i in l :
    print(i.id ,i.deadline,i.profit)
    
    """

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        Jobs.sort(key = lambda x:(x.deadline,x.profit),reverse=True)
        
        cnt = 1
        profit= Jobs[0].profit
        for i in Jobs :
            print(i.id ,i.deadline,i.profit)
        for i in range(1,len(Jobs)):
            if Jobs[i-1].deadline == Jobs[i].deadline :
                continue
            else:
                cnt+=1
                profit+= Jobs[i].profit
                
        return [cnt,profit]
    
    
a = Solution()
a.JobScheduling(l,len(l))
            
            
