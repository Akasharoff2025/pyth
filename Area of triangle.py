a=int(input("Enter the limit:"))
f0=0
f1=1
print(f0)
print(f1)
for i in range(0,a-2):
    f=f0+f1
    print(f)
    f0=f1
    f1=f
