'''Program 4: WAP to display following pattern:
12345
 2345
  345
   45
    5
'''
a=int(input("no of rows: "))
for i in range(1,a+1):
    print(" "*(i),end="")
    for j in range(i,a+1):
        print(j,end="")
    print()