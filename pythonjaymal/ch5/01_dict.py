a={"harry":1,
   "jayant":100,
   "tanish":0,
   "nilu":69}
print(a,type(a))
print(a.items())
print(a.keys())
print(a.values())
a.update({"harry":99,"niru":9})
print(a)
print(a.get("harry"))#if key doesnot exist in the dict it will return none
print(a["harry"]) #if key doesnot exist in the dict it will return an error
b=a.pop("nilu",69)
# print(b)
print(a)
c=a.popitem()
print(a)