size = int(input("Enter the size of the pattern: "))
a = size

while size > 0:
    # This is the outer loop
    for i in range(a):
        print("*", end="")
    print()
    size -= 1
