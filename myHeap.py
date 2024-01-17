class Heap :
    def __init__(self)  :
        self.arr= []
        
    def parent(self,i) :
        return (i-1)//2
    
    def lchild(self,i) :
        return 2*i+1 
    def rchild(self,i) :
        return 2*i+2
    
    def insert(self,val) :
        self.arr.append(val)
        i = len(self.arr)-1
        while i > 0 and self.arr[self.parent(i)] > self.arr[i]:
            self.arr[self.parent(i)] ,self.arr[i] =  self.arr[i],self.arr[self.parent(i)] 
            i = self.parent(i)
    
    
    def heapify(self, i) :
        if i > len(self.arr) :
            return 
        l = self.lchild(i)
        r = self.rchild(i)
        sml = i 
        
        if  l < len(self.arr) and self.arr[sml] > self.arr[l] :
            sml = l
        if r < len(self.arr) and self.arr[sml]> self.arr[r] :
            sml = r
        if sml != i :
            self.arr[i], self.arr[sml] = self.arr[sml] , self.arr[i]
            i = sml 
            self.heapify(sml)
            
    def extractMin(self):
        res = self.arr[0]
        self.arr[0],self.arr[len(self.arr)-1] = self.arr[len(self.arr)-1] , self.arr[0]
        self.arr.pop()
        self.heapify(0)
        return res
    
    
    def printH(self):
        print(*self.arr)
        
        
        
    
        
        
        
        
a= Heap()
a.printH()
for i in [20,25,30,40,80,32,100,70,60]:
    a.insert(i)
    
a.printH()
a.extractMin()
a.printH()
        
        
        
        
            
        