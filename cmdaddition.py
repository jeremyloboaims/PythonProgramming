import sys


def add(n, m):
    print("Addition of", n, "and", m, "is:", (m + n))


n = int(sys.argv[1])
m = int(sys.argv[2])
add(n, m)