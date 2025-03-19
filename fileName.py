from math import e


def Creat_fileName(k,i='.py'):
    j = "_".join(k.split(" " ))
    return j + i
    
def Creat_array(k ,t ="int"):
    j = k.split(" ")
    if t == "int":
        for i in range(len(j)):
             if type(j[i]) == str:
                j[i] = int(j[i])
    
    print(j)


k = "207"
j = Creat_fileName(k,".cpp")
try :
    with open(j,'x') as f:
        f.write("#File create\n")
    print(f'{j} created')
except FileExistsError:
    print(f"{j} already exists")
