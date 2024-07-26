k = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]

row = len(k)
col = len(k[0])

for i in range(col):
    for j in range(row):
        print(k[j][i])
    print("________________________")