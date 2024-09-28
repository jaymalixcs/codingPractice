'''Program 2: WAP to check whether a number is prime or not?'''
a=int(input("Enter a number:"))
for i in range(2,a):
    if a%i==0:
        print("Its Not a Prime Number")
        break
else:
    print("Its a Prime Number")