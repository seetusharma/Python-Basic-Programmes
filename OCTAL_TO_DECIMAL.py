num=int(input("Enter a octal number"))
rem=0
decimal=0
i=0
while num!=0:
    rem=num%10
    decimal = decimal+rem*pow(8,i)
    num=num//10
    i+=1
print(decimal)
