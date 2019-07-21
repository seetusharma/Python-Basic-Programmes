num=int(input("Enter a binary number: "))
rem=0
decimal=0
i=0
while num!=0:
    rem=num%10
    decimal=decimal+rem*pow(2,i)# we can also use "pow" function
    num=num//10
    i=i+1

print(decimal)
    
