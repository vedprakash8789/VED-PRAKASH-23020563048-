a=int(input("Enter the coefficients of the quadratic equation for base x^2"))
b=int(input("Enter the coefficients of the quadratic equation for base x"))
c=int(input("Enter the coefficients of the quadratic equation for constant"))
root1= (-b+(((b**2)- 4*a*c)**0.5))/2*a
root2= (-b-(((b**2)- 4*a*c)**0.5))/2*a
print("the roots of the given quadratic equation",a,"x^2 +",b,"x +",c,"is ",root1,root2)
