def validate_name(name):
    if any(char.isdigit() for char in name):
        raise ValueError("Name should not contain digits.")
    if not name.isalpha():
        raise ValueError("Name should not contain special characters.")

    return name

try:
    user_input = input("Enter your name: ")
    
    validated_name = validate_name(user_input)
    
    print("Your name:", validated_name)

except ValueError as ve:
    print(f"Invalid input: {ve}")
