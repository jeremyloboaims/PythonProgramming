def search(arr):
    x = int(input("Enter a number to search for: "))
    if x in arr:
        print("Yes,", x, "is in the list.")
        pos = arr.index(x)
        print("Index of", x, "in list is", pos, ".")
    else:
        print("No,", x, "is not in the list.")


numbers = []
n = int(input("Enter the number of elements in your list: "))
for i in range(0, n):
    a = int(input("Enter a number to add to the list: "))
    numbers.append(a)
search(numbers)

