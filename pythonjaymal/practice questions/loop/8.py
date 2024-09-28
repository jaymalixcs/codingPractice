'''Program 8: WAP to ask user to enter two numbers and find sum of numbers in between those two numbers.'''
a=int(input(""))
b=int(input(""))
sum=0
for i in range(a+1,b):
    sum+=i
print(sum)