'''Program 1: WAP to calculate factorial of a number.'''
a=int(input("Enter a number: "))
product=1
for i in range(1,a+1):
    product*=i
print(product)