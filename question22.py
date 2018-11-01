
no=int(input("enter a number:"))
fac=1
if no<=0:
    print("no factorial")
else:
     for x in range(1,no+1):
         fac=fac*x
print("the factorial of", no,"is",fac)