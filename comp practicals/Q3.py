def pyramid():
    for i in range(1, 5 + 1):
        for j in range(5 - i):
            print(" ", end="")
        for k in range(2 * i - 1):
            print("*", end="") 
        print()

def inverse_pyramid():
    for i in range(5,0,-1):
        for j in range(0,5-i):
            print(" ", end="")
        for k in range(2 * i - 1):
            print("*", end="") 
        print()

pyramid()
print()
print()
inverse_pyramid()

