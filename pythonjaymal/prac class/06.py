principal =int(input("Enter the principal:"))
rate =float(input("Enter the rate: "))
term =int(input("Enter the term:"))
totalinterest = 0
i=0
while i<=term:
    interest=principal*rate
    print(interest)
    principal+=interest
    totalinterest+=interest
    i+=1
print("Total interest is:",totalinterest)
print("principal is:",principal)