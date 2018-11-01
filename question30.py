no=int(input("enter a number:"))
sum=0
while no!=0:
    r=no%10
    no=no//10
    sum+=r
print("the sum of digits =",sum)