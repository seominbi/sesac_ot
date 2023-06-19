for i in range(2,10):
    print("%s단" %i)
    for j in range(1,10):
        print("%s * %s = %s" %(i, j ,(i*j)))
    print("\n")


def gugudan():
    for i in range(2,10):
        print("%s단" %i)
        for j in range(1,10):
            print(f"{i} * {j} = {i*j}")

gugudan()


