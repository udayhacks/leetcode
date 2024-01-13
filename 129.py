class Solution:
    def sumNumbers(self, root) -> int:

        ans = [0]

        def tree_traversal(root, curr, ans):
            k = root.data
            curr += str(k)

            if root.left == None and root.right == None:
                ans[0] = ans[0] + int(curr)
                return

            if root.left:
                tree_traversal(root.left, curr, ans)
            
            if root.right:
                tree_traversal(root.right, curr, ans)
        
        tree_traversal(root, '', ans)
        return ans[0]    
class node:
    def __init__(self ,data):
        self.left = None 
        self.data = data 
        self.right = None 
        
        
k = [1,2,3,4,5,6,7,8,9]
a = node(1)
b = node(2)
c = node(3)
d = node(4)
e = node(5)
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

"""a = Solution()
a.sumNumbers(root) 


"""
















class Solution:
    def findSecondMinimumValue(self, root) -> int:
        if not root:
            return -1

        stack = [root]
        first_min = float('inf')
        second_min = float('inf')

        while stack:
            current = stack.pop()
            if current.val < first_min:
                second_min = first_min
                first_min = current.val
            elif current.val < second_min and current.val != first_min:
                second_min = current.val

            if current.left:
                stack.append(current.left)
            
            if current.right:
                stack.append(current.right)
            
        
        return second_min if second_min != float('inf') else -1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def second(root,f= float("inf"),s=float('inf')) :
    
    if root :
   
      
        if root.data < f:
            s =f
            f= root.data
        elif root.data < s and s != f :
            s = root.data 
            
        second(root.left , f,s) 
        second(root.right,f,s)
            
        return s 



print(second(root))