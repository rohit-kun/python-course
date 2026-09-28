# program that takes two numbers and print their sum, difference, product and whethere the number is greatter than the second

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

sum = a+b
difference = a-b
product = a*b
greater = a>b

print(f"sum is: {sum}\ndifference is: {difference}\nproduct is: {product}\ngreater is: {greater}")