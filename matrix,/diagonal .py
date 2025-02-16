
l = [[1,7,3],[9,8,2],[4,5,6]]
n = len(l)

for i in range(n) :
    for j in range(n) :
        print(l[i][j], " " ,end ="")
    print()
print(" ........................................")
for i in range(0,n) :
    for j in range(i,n) :
            print(l[j][j-i], " ",end ="")
    print()

for i in range(0,n) :
    for j in range(0,n-i) :
            print(l[j][j+i], "  " ,end ="")
    print()
