

def ins(lst , jl ) :
    n = len(lst) 
    
    if n ==1 :
       if lst[0][0] <l[0]:
            lst.append(l)
       else:
            lst.insert(0, l)
        
    else:
        
        if lst[0][0] > jl[0]  :
            lst.insert(0,l) 
        else:
            for i in range(0,n-1):
                if lst[i][0] <l[0] < lst[i+1][0] :
                    break 
            lst.insert(i+1, l)
            
                    
            
    
      

#n = 7   ....012345



k = [[1,5],[6,8]]
l=[0,9]



ins(k , l)