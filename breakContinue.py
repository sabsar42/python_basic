while True:
    n = input("entr=")
    n = int(n)

    if n<0:
        print("only pstv")
        continue
    elif n==0:
        break
    else:
        print("sq of",n,"is",n*n)