
l = [2,3,10]
arr = [-1]*sum(l)
i = 0
l.sort(reverse=True)
n = sum(l)
while True :
    k = l[0]
    
    while k >= 0 and i < n  :
        arr[i] =l[0] 
        k-=1 
        i+=2
        
    if k > 0 :
      print("no")
      break
      
    k = l[1]
    i = 1
    
    while k>= 0 and i <n  :
        arr[i] =l[1] 
        k-=1 
        i+=2
        
    if k > 0 :
      print("no")
      break
    else:
      print("yes")
      break
      
        
        
        
        
        