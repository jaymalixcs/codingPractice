a=int(input("No of units consumed by user: "))
if a>0:
    if a<=200:
        c=a*2
        print("Electricity billis",c)
    elif a>200 and a<=400:
        d=200*2+(a-200)*4
        print("Electricity bill = ",d)