'''Program 4: WAP to show following conditions using nested if else statement:
	gender: male	salary>10000 then bonus should be 1000
			salary <10000 and >5000, then bonus=500
			s
alary <5000, then bonus=100
	gender:female	salary>10000 then bonus should be 100
			salary <10000 and >5000, then bonus=50
			salary <5000, then bonus=10
'''
gender=input("Gender:")
salary=int(input("salary: "))
a=gender.capitalize()
if a=="Male" and salary>0:
    if salary>10000:
        print("Bonus is 1000")
    elif salary<10000 and salary>5000:
        print("Bonus is 500")
    else:
        print("Bonus is 100")
elif a=="Female" and salary>0:
    if salary>10000:
        print("Bonus is 100")
    elif salary<10000 and salary>5000:
        print("Bonus is 50")
    else:
        print("Bonus is 10")
else:
    print("Invalid input")