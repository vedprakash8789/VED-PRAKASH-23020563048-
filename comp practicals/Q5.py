while True:
    str1=str(input("ENTER A STRING"))
    while True:
            choice=int(input("Enter 1 to display the lenght of the string , 2 to replace a string ,3 to remove the first occurence of a string and 4 to remove all the occurences of the string"))
            if choice==1:
                print(len(str1))
            elif choice==2:
                ch1=str(input("enter the string to be replaced"))
                ch2=str(input("enter the new string to be replaced"))
                str2=str1.replace(ch1,ch2)
                print(str2)
            elif choice==3:
                ch1=str(input("enter the character whose first occurence is to be removed "))
                l=str1.index(ch1)
                str2=str1[:l:]+str1[l+1::]
                print(str2)
            elif choice==4:
                ch1=str(input("enter the character which is to be removed "))
                str2=str1.replace(ch1,'')
                print(str2)
            else :
                print("invalid choice")
            opt=str(input("enter y to choose different operations on same string n to continue to menu"))
            if opt=='n':
                break
    opt2=str(input("enter y to start with beginning and n to quit"))
    if opt2=='n':
        break
    
