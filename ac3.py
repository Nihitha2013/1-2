def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

num=int(input("Enter number:"))
if num<0:
    print("Not exit for negative number")
else:
    print("Factorial:",fact(num))
    