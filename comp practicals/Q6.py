str1= input("enter the first string")
str2= input("enter the second string")
n=int(input("enter the number for swapping"))
if n>len(str1) or n>len(str2):
    print("n exceeded the lenght to string")
else :
    str3=str1[:n+1:]+str2[n+1::]
    str4=str2[:n+1:]+str2[n+1::]
    print("the string after swapping are",str3,str4)
