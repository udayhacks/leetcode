

n , m = map(int, input().split()) 
a = {}
for i in range(m):
    k , j = map(int,input().split())   
    if k in a : 
        a[k].append(j)
    else:
        a[k]=[j] 
    if j in a : 
        a[j].append(k)
    else:
        a[j] = [k]

t, o , tt = 0 , 0 , 0 


for i ,j in a.items():

    if len(j) ==1 :
        o+=1
    elif len(j) ==2 :
        tt+=1
    elif len(j) ==n-1:
        t+=1
        
      
if n == tt :
    print("ring topology")
    

elif n-2 == tt and o == 2 :
    print("bus topology")
    
elif t == 1 and o == n-1:
    print("star topology")
    
else:
    print("unknown topology")

