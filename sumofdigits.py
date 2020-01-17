def sumofdig(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum = sum + digit
        n = n // 10
    print("Sum of the digits of the number:", sum)


n = int(input("Enter number: "))
sumofdig(n)