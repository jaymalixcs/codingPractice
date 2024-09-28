a=int(input(""))
for i in range (a,0,-1):
    print(" "*(a-i),end="")
    print("*"*(2*i-1),end="")
    print(" "*(a-i),end="")
    print("")