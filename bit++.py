
t = int(input())
x= 0 
while t:
    s = input()
    if s[0]== 'X' and  s[1] == '+' or s[0]=='+':
        x+=1
    else:
        x-=1
    t-=1
        
print(x)


    
    