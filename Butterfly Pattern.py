def symmetry(n: int):
    for i in range(1,n):
        for s in range(i):
            print("* ",end= "")
        for sp in range(n-i):
            print("  ",end="")
        for sp in range(n-i):
            print("  ",end="")
        for s in range(i) :
            print("* ",end= "")
        print()

    for i in range(n,0,-1):
        for s in range(i) :
            print("* ",end= "")
        for sp in range(n-i):
            print("  ",end="")
        for sp in range(n-i):
            print("  ",end="")
        for s in range(i) :
            print("* ",end= "")

        print()

symmetry(3)