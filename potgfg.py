class Solution:
    def printPaths(self, root, sum):
        
        def helper(ans,path,sum ,root):
            
                if root is None :
                    return 
                aa= root.data
                sum-=root.data
                path.append(root.data)
                if sum==0 :
                    ans.append(path[:])
                if root.left :
                    helper(ans,path,sum,root.left)
                if root.right:
                    helper(ans,path,sum,root.right)
                    
                path.pop()
                    
                    
        ans = []
        path = []
        
        helper(ans,path,sum,root)
        return ans 
            
            
class node:
    def __init__(self ,data):
        self.left = None 
        self.data = data 
        self.right = None 
                    
k = [1,2,3,4,5,6,7,8,9]
a = node(1)
b = node(1)
c = node(3)
d = node(4)
e = node(2)
g = node(6)
f = node(7)
h = node(8)
i = node(9)

root = a
root.left = b
root.right = c 
b.left = d
b.right= e
c.left = g
c.right= f 
d .left = f 
d.right  = h
e.left = i




a= Solution()
a.printPaths(root,4)








            