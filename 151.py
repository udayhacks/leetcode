
s = "the sky is blue"

s = "  hello world  "
k = list(s.split(" "))
l= []

for i in k :
    if i != "":
        l.append(i)
        
        
ans = "blue is sky the"
s = ""
n = len(l)


for i in range(len(l)-1,-1, -1):
    s+=l[i]
    s+=" "
    



    
if ans == s :
    print("yes")



s = "the sky is blue"
s = "  hello world  "
ll=[]




for i in s.strip().split():
    ll.append(i)
    
    
k = "".join(ll[::-1])
    

