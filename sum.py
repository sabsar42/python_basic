while True:
    #bcz of whilw it will always ask for input 
    n = input("plz entr no= (o to exit) ")
    #input 0 break will run
    n = int(n)

    if n == 0:
        break
    print("square of ", n, "is",n*n )