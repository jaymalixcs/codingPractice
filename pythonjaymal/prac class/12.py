a=int(input(""))
b=input("")
c=b.split()
# print(c)
c.append(str(a))
# print(c)
for i in range(0,len(c)):
    d=c[i]
    e=d[::-1]
    if d==e:
        print(d)
        break
else:
    print(-1)
        