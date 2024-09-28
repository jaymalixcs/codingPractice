'''Program 5: WAP to display all numbers between 20 and 60 except printing numbers which are divisible by 7.'''
a=int(input(""))
b=int(input(""))
list=[]
for i in range(a,b+1):
    if i%7==0:
        continue
#     else:                           
#         list.append(i)
# print(list)
#if we want to convert into list
    else:
        print(i)