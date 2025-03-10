from turtle import right


a = 1
b = 4 



def func(a,b,l):
    if a <= 0 or b <= 0:

        return 0
    l.append((a,b))
    left = 1+func(a-2,b+1,l)
    right = 1+func(a+1,b-2,l)
    
    return max(left,right)
l = []
print(func(a,b,l))
print(l)