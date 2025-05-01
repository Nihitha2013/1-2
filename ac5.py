num1= int(input("Enter the first number:"))
num2= int(input("Enter the second number:"))

ch= input("Enter operation (+, -, *, /): ")

result=0
if ch == '+' :
    result=num1 + num2
elif ch == '-':
    result=num1 - num2
elif ch == '*':
    result=num1 * num2
elif ch == '/':
    result=num1 / num2

print(num1, ch, num2, ":", result)