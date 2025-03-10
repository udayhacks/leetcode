def Creat_fileName(k):
    j = "_".join(k.split(" " ))
    print(j)
    
def Creat_array(k ,t ="int"):
    j = k.split(" ")
    if t == "int":
        for i in range(len(j)):
             if type(j[i]) == str:
                j[i] = int(j[i])
    
    print(j)





Creat_fileName("Sieve of Eratosthenes")
Creat_fileName("Count increasing Subarrays")