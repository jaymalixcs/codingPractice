'''Program 7: WAP to print A-Z n the form of AB   CD   EF....'''
for i in range(1,27,2):
    print(chr(64+i),end="")
    print(chr(64+i+1),end=" ")