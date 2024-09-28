'''Program 9:WAP to ask user to enter a number and display multiplication table in the form of
N*1=....
N*2=....
.
.
N*10=.....
'''
n=int(input(""))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")