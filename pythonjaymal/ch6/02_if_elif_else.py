
a=int(input("enter your age: "))
if(a>=18):
    print("You are above the age of consent")
elif(a<0):
    print("You are entering an invalid negative age")
elif(a==0):
    print("you are 0")
else:
    print("You are below the age of consent")

print("End of Program")