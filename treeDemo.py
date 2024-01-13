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


def rr(root, l = []) :
            if root :
                l.append(root.data)

                if root.right and root.right.right :
                    rr(root.right,l)



                else :
                    if root.right :
                        l.append(root.right.data)

                    if root.left and root.left.right :
                        rr(root.left.right,l)

                    elif root.left and root.left.left :
                        rr(root.left.left,l) 
                    elif root.right is None:
                        rr(root.left.l)

                return l
            
            
            
class Solution:
    def averageOfLevels(self, root) :

        ans = []
        q = []
        j =[]
        q.append(root)
        j=[root.data]


        while q:
            k = len(q)
            s = 0 
            ans.append(sum(j)/len(j))
            for i in range(k):
                g = q.pop()
                j.pop(0)
                
                if g.left :
                    q.append(g.left)
                    j.append(g.left.data)
                    
                if g.right :
                    q.append(g.right)
                    j.append(g.right.data)

            

        return ans 

a= Solution()
print(a.averageOfLevels(root))