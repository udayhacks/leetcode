class Heap :
    def __init__(self,l =[])  :
        
        #build heap 
        self.arr= l
        i = (len(l)-2)//2
        while i >= 0 :
            self.heapify(i,len(l))
            i = i-1  
                 
    def parent(self,i) :
        return (i-1)//2
    
    def lchild(self,i) :
        return 2*i+1 
    def rchild(self,i) :
        return 2*i+2
    
    def insert(self,val) :
        aa = self.arr
        # In insertion the val is inserted in the end and it swap the parents and val
        self.arr.append(val)
        i = len(self.arr)-1
        while i > 0 and self.arr[self.parent(i)] > self.arr[i]:
            self.arr[self.parent(i)] ,self.arr[i] =  self.arr[i],self.arr[self.parent(i)] 
            i = self.parent(i)
    
    
    def heapify(self, i,n) :
        
        # these functions adjust the heap  second relation i.e  parent.val is always less than its parent.left.val and parent.right.val
        aa = self.arr
        if i > len(self.arr) :
            return 
        l = self.lchild(i)
        r = self.rchild(i)
        sml = i 
        
        if  l < n and self.arr[sml] > self.arr[l] :
            sml = l
        if r < n and self.arr[sml]> self.arr[r] :
            sml = r
        if sml != i :
            self.arr[i], self.arr[sml] = self.arr[sml] , self.arr[i]
            i = sml 
            self.heapify(sml,n)
            
    def extractMin(self):
        # here we swap 0 index with last index due to O(1) time complexity
        
        res = self.arr[0]
        self.arr[0] ,self.arr[len(self.arr)-1] = self.arr[len(self.arr)-1] , self.arr[0]
        self.arr.pop()
        self.heapify(0,len(self.arr))
        return res
    
    
    def decrese_key(self,i,val) :
        # decrease is same like insertion task .............
        
        self.arr[i] = val
        while i > 0 and self.arr[self.parent(i)] > self.arr[i]:
            self.arr[self.parent(i)] ,self.arr[i] =  self.arr[i],self.arr[self.parent(i)] 
            i = self.parent(i)
    
    def heapSort(self):
        aa= self.arr
        
        n =len(self.arr)
        for i in range(n-1 ,-1,-1):
            self.arr[i],self.arr[0] = self.arr[0],self.arr[i]
            self.heapify(0,i)
            
        
    
    
    def printH(self):
        print(*self.arr)
        
        
        
        
        
        
        

a = Heap()
for i in [2,1,4,56,8]:
    a.insert(i)
a.printH()
a.heapSort()
a.printH()


        
        
        
        
    
   
        
            
        