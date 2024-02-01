
l = "jijiji c"
k = list(l)
n = len(k)
h= 0
if k[-1] in k[:n-2] :
    for i in range(len(k)-1):
        if k[-1] ==k[i] :
            h = i

    k = k[0:len(k)-2]
    i = h
    j = n-3
    while i <j :
        k[i],k[j] = k[j],k[i]
        i+=1
        j-=1


    print("".join(k))
    
else:
    print("".join(k[0:len(k)-2]))