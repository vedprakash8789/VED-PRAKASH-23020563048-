def cubes_dict():
    cube = {key: key**3 for key in range(1, 6)}
    
    for key, value in cube.items():
        print(f"{key}: {value}")

cubes_dict()
