def prnt(n):
    if n <= 0 :
        return 
    prnt(n-1)
    print(n) 
      
prnt(12)