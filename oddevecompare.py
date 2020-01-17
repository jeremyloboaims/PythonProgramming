def comp(a, b):
    if a > b:
        print("Sum of odd numbers is greater than even.")
    elif a < b:
        print("Sum of even numbers is greater than odd.")
    else:
        print("Both sums are equal.")


def add(a):
    even = 0
    odd = 0
    for x in a:
        if (x % 2) == 0:
            even = even + x
        else:
            odd = odd + x
    print("The sum of odd numbers is", odd, "and sum of even numbers is", even)
    comp(odd, even)


numbers = []
n = int(input("Enter the number of elements in your list: "))
for i in range(0, n):
    a = int(input("Enter a number to add to the list: "))
    numbers.append(a)
add(numbers)


