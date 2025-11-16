
size = int(input("Enter the size of the pattern: "))
row = 0

while row < size:
    for i in range(size):
        print("*", end="")
    
    print()
    
    # Increase the row count
    row += 1
