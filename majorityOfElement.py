l = [8,3,4,8,8]
def majority(l):
    h = {}
    res = 0
    for i in l :
        if i in h:
            h[i] +=1
            if h[i] > len(l)//2:
                return i
        else :
            h[i] =1

majority(l)
    


        