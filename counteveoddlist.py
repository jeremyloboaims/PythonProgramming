def count(a):
    even = 0
    odd = 0
    for x in a:
        if(x % 2) == 0:
            even = even + 1
        else:
            odd = odd + 1
    print("The number of odd numbers is",odd,"and even numbers is",even)


def add(a):
    even = 0
    odd = 0
    for x in a:
        if (x % 2) == 0:
            even = even + x
        else:
            odd = odd + x
    print("The sum of odd numbers is", odd, "and sum of even numbers is", even)


numbers = []
n = int(input("Enter the number of elements in your list: "))
for i in range(0,n):
    a = int(input("Enter a number to add to the list: "))
    numbers.append(a)
count(numbers)
add(numbers)


