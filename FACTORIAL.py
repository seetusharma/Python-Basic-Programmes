# without recursion
num=int(input("Enter a number"))
fac=1
for i in range(1,num+1):
    fac=fac*i
print(fac)

#with recursion
def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)

print(fac(num))
