def isprime (j):
    c=0
    for i in range (1,j+1):
        if j%i==0:
           c=c+1
    if c==2:
        print(j,"is prime")
    else:
        print(j,"not a prime")
def primetilln(j):
    print("ALL THE PRIME NUMBER TILL N ARE :-")
    for i in range (1,j+1):
        c=0
        for k in range (1,i+1):
            if i%k==0:
                c=c+1
        if c==2:
            print(i)

        
def firstnprime(j):
    print("FIRST N PRIME NUMBER  ARE")
    i=1
    d=0
    while d<j :
        c=0
        
        for k in range (1,i+1):
            if i%k==0:
                c=c+1
        if c==2:
            print(i)
            d=d+1
        i=i+1
             

        
        

n=int (input ("ENTER A NUMBER "))
isprime(n)
primetilln(n)
firstnprime(n)
