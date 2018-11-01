no=int(input("enter any number:"))
if no>1:
    for n in range (2,no):
        if (no%n):
            print(no,"is not a prime number")
            break
    else:
        print(no,"is prime number")
else:
    print("no is not prime number")

