n = int(input("enter number: "))
i = 1
c = 0
while i<=n:
    if n%i==0:
        print(i)
        c = c+1
    i+=1
print(c)

if c==2:
    print("prime")

else:
    print("non prime")