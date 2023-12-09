ch=input("enter a character")
if ch.isalpha():
    print(ch,"is a letter")
    if ch.isupper():
        print("It is in upper case")
    else:
        print("It is in lower case")
elif ch.isdigit():
    print(ch,"is a digit")
    import inflect
    p = inflect.engine()
    print(p.number_to_words(ch))
