class Solution:
    def simplifyPath(self, path: str) -> str:
        pathList = path.split("/")
        stack = [] 
        for i in pathList :
            if stack and i == '..' :
                stack.pop()
            elif i != "" and i != "."  and i != '..':
                stack .append(i)
                
        return "/"+"/".join(stack) 
                
        
  
 


        
a = Solution()
a.simplifyPath("/../")
a.simplifyPath("/home//alpha")
a.simplifyPath("/a/../../b/../c//.//")