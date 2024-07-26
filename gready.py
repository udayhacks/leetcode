r = 5 
e = 3 
rr = [1,4,3,2]
ee = [2,6,4,2]

def func(r,e,rr,ee):
    
        t = 0 
        
        for i in range(len(rr)) :
            if rr[i] < r :
                r -=rr[i]
            elif rr[i] >= r :
                t+=(rr[i]-r)+1
                break
        
        t+=(sum(rr[i+1:]))
        
        k = 0 

        for i in range(len(ee)) :
            if e > ee[i] :
                e+=ee[i]
            elif e <= ee[i]:
                l = (ee[i]-e)+1
                k+=l
                e = e+l+ee[i]
        
        
        return t,k              


t,k = func(r,e,rr,ee)




t+=r
k+=3

for i in rr :
    if t > i :
        t-=i 
        print(t) 
    else:
        print("FAIL")

    
    
    
for j in ee :
    if k> j :
        k+=j 
        print(k) 
    else:
        print("FAIL")

    

    

        

