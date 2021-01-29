def MonAddTable(n):
    print()
    print("Modulo Addition Table(%d) is :" % n)
    print('i,j',end=" ")
    for j in range(n):
        print("%4d" %j,end=" ")
    print()
    res=0
    for i in range(n):
        print("%4d" %i,end=" ")

        for j in range(n):
            res = (i+j)%n
            print("%4d"% res ,end = " ")
        print()
    print()

def MonMulTable(n):
    print()
    print("Modulo Mulition Table(%d) is :" % n)
    print('i,j',end=" ")
    for j in range(n):
        print("%4d" %j,end=" ")
    print()
    res=0
    for i in range(n):
        print("%4d" %i,end=" ")

        for j in range(n):
            res = (i*j)%n
            print("%4d"% res ,end = " ")
        print()
    print()
if __name__ == '__main__':
    MonAddTable(13)
    MonMulTable(19)
    

    