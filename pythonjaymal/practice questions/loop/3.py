'''Program 3: WAP to reverse a given number,it can be of any number of digits.'''
a=int(input(""))
num=0
while a!=0:
    digit=a%10
    num=num*10 +digit
    a//=10
print(num)
    