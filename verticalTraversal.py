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






from collections import deque ,OrderedDict
def verticalTraversal(root) :
    if root is None :
        return root 
    
    hash= {}
    x = []

    
    q = deque()
    q.append(root)
    x = [0]
    
    while q :
        curr = q.popleft()
        hd = x.pop(0)
        
        if hash.get(hd) == None :
            hash[hd] = []
            
        hash[hd].append(curr.data)
        
        if curr.left :
            q.append(curr.left)
            x.append(hd-1)
        if curr.right:
            q.append(curr.right)
            x.append(hd+1)  
            
            
            
            
    k = (sorted(hash))
<<<<<<< HEAD
    #print(k)
=======
    print(k)
>>>>>>> main
    
    
    for i in k :
        for j in hash[i] :
            print(j,end = "")
            
            
            
verticalTraversal(root)
        
        