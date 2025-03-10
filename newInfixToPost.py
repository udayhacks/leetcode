
class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, s):
        
        dic= {
            '^' : 3 ,
            '*' : 2 ,
            '/' : 2 ,
            '+' : 1 ,
            '-' : 1 ,
            '(' : 0 ,
        }
        
        
        ans = ""
        stack = []
        
        for i in s :
            
            if i.isalpha():
                ans+=i
            elif i =='(':
                stack.append("(")
            elif i == ")":
                while stack and stack[-1]!= '(':
                    ans+=stack.pop()
                stack.pop()
            else:
                if stack and dic[stack[-1]] >= dic[i]:
                    ans+=stack.pop()
                    
                stack.append(i)
            
            
            
            
        while stack:
            ans+=stack.pop()       
                
        return ans 
                
                    
    
            
        
        
a = Solution()
print(a.InfixtoPostfix("a+b*(c^d-e)^(f+g*h)-i"))