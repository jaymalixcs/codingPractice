a=input("You want to find area of: ")
b=a.capitalize()
if b=="Rectangle":
    l=int(input("L: "))
    b=int(input("B: "))
    print('Area is',l*b)
elif b=="Circle":
    c=int(input("R: "))
    print('Area is',3.14*c*c)
elif b=="Square":
    s=int(input("S: "))
    print("Area is",s*s)
else:
    print("Invalid Input")