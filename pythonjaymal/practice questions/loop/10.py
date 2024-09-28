'''Program 10: WAP to ask user to enter numbers 10 times , count how many of them are positive, how many are negative and how many zeros.'''
positive=0
negative=0
zereos=0
for i in range(1,11):
    a=int(input(""))
    if a > 0:
        positive+=1
    elif a < 0:
        negative+=1
    else:
        zereos+=1
print("The no of positive =",positive)
print("The no of negative =",negative)
print("The no of zereos =",zereos)
    