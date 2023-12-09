def cube(input):
    result = []
    for element in input:
        if isinstance(element, int) and element % 2 == 0:
            result.append(element ** 3)
    return result


inp = []
for i in range(20):
    inp.append(int(input("enter the elements of list")))
output= cube(inp)
print(output)
