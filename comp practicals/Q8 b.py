def cube(inp):
    return [element ** 3 for element in inp if isinstance(element, int) and element % 2 == 0]


inp = [1, 2, 3, 4, 5, "a", 6, 7, 8, "b", 9, 10]
output = cube(inp)
print(output)
