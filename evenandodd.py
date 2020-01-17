def evenodd(n):
    if ((n % 2) == 0):
        print("{} is an even number".format(n))
    else:
        print("{} is an odd number".format(n))

def prime(n):
    if(n == 1):
        print("One is neither prime nor composite")
    else:
        for i in range(2,n,1):
            if((n % i) == 0):
                print("{} is not a prime number".format(n))
                break
        else:
            print("{} is a prime number".format(n))


n = int(input("Enter a number: \n"))
evenodd(n)
prime(n)