n = int(input())

row = 1
while row <= n:
    print(" " * (n - row), end="")
    if row == 1 or row == n:
        print("*" * n, end="")
    else:
        print("*", end="")
        print(" " * (n - 2), end="")
        print("*", end="")
    print()
    row += 1

