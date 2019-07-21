def factorial(n):
    fac=1
    for i in range(1,n+1):
        fac=fac*i
    return fac
n1=int(input("Enter the upper range: "))
n2=int(input("Enter the lower range:"))
print("Strong Number","between",n1,"and",n2,":")
for i in range(n1,n2+1):
    num2=i
    rem=0
    s=0
    while(i!=0):
        rem=i%10
        s=s+factorial(rem)
        i=i//10
    if(num2==s):
        print(s)

