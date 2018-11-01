while True:
    while True:
        n = int(input("Enter n (integer expected): "))
        if n < 1:
            pass
        elif n >3000:
            print("This number is too large to be computed.")
            pass
        else:
            break
    for i in range(1,n):
        n = n*i
    print('The factorial of n is ',n,'.00.')
    break


    
