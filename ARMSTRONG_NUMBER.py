def cube(n):
    return n**3

n1=int(input("Enter the upper range"))
n2=int(input("Enter the lower range"))
print("Armstrong number between the range",n1,"and",n2,":")
for i in range(n1,n2+1):
    num2=i
    rem=0
    arm=0
    while(i!=0):
        rem=i%10
        arm=arm+cube(rem)
        i=i//10
    if(num2==arm):
            print(arm)
else:
    print("Not more Armstrong Number")
