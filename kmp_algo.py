def lpsf(pttn) :
    n = len(pttn)
    l = 0 
    lp= [0]*n
    i = 1 
    # match for last matched prefix in the pattern . 
    while i < n :
        if pttn[i] == pttn[l] :
            lp[i] = l+1
            i+=1
        else:
            if l != 0 :
                l = lp[l-1]
            else:
                lp[i]  = 0 
                i+=1
    return lp 






def kmp(num, ptn) :
    
    i = 0 
    j = 0 
    lps = lpsf(ptn) 
    
    n = len(num)
    m = len(ptn )
    
    while i < n :
        if num[i] == ptn [j] :
            i +=1
            j +=1
            
        else :
            if j != 0 :
                j = lps[j-1]
            else:
                i +=1
        if j == m :
            print("pattern matched at Index ", (i-j, i))
            j = lps[j-1]




nums = "wrtrtyudayrt"
ptn = "uday"


kmp(nums,ptn)
    
    
    
             
            