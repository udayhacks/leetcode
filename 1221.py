class Solution:
    def balancedStringSplit(self, s):
        ans = 0 
        c = 0 
        for i in s :
            if i == "L":
                c-=1 
            elif i == "R":
                c+=1
            if c == 0 :
                ans+=1

        return ans 
            
        

k = ["RLRRLLRLRL","RLRRRLLRLL","LLLLRRRR"]

a= Solution()

for i in k :
    print(a.balancedStringSplit(i))