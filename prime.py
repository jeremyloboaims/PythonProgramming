def prime(n,m):
    if(m < 2):
        print("Invalid range")
    else:
        for i in range(n,m):
            for j in range(2,i,1):
                if((i % j) == 0):
                    break
            else:
                print(i)


n = int(input("Enter the start of your range: \n"))
m = int(input("Enter the end of your range: \n"))
prime(n,m)