a=input("")
b="password"
count=1
while True:
    if a==b:
        count+=1
        print('You have successfully logged in.')
        break
    elif a!=b:
        if count<3:
            count+=1
            a=input("Wrong password. Try again. ")
        else:
            print("You have been denied access.")
            break
