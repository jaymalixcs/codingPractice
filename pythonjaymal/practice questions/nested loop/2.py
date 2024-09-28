'''Program 2: WAP to display following pattern:
        1
      12
    123
  1234
12345
'''
a=int(input("no of rows: "))
for i in range(1,a+1):
    print("  "*(a-i),end="")
    for j in range (1,i+1):
        print(j,end="")
    print()