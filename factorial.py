def factorial(n):
    fact = 1
    for i in range(1,(n+1)):
        fact = fact * i
    print("The factorial of {} is {}".format(n,fact))

n = int(input("Enter a number: \n"))
factorial(n)