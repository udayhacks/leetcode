pattern = "abba"
s = "dog cat cat dog"
k = s.split(" ")
pattern  = list(pattern) 

for i , j in zip(k , pattern) :
    print(i , j )



print(k)
print(pattern)
l = [1,2,3]
k = [4,5,6]
for i ,j in zip(l,k):
    print(i , j)

        
        