def tuple_operations():
    t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
    half_length = len(t1) // 2
    print("Half of the values:", t1[:half_length])
    print("Other half of the values:", t1[half_length:])
    even_numbers_tuple = tuple(num for num in t1 if num % 2 == 0)
    print("\nTuple with even numbers:", even_numbers_tuple)
    t2 = (11, 13, 15)
    concatenated_tuple = t1 + t2
    print("\nConcatenated tuple:", concatenated_tuple)
    max_value = max(t1)
    min_value = min(t1)
    return max_value, min_value
result = tuple_operations()
print("\nMaximum value:", result[0])
print("Minimum value:", result[1])
