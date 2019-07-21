num=int(input("Enter a number in binary"))
rem=0
dec=0
octal=""
i=0

#First convert the number into Decimal

while num!=0:
    rem=num%10
    dec=dec+rem*pow(2,i)
    num=num//10
    i=i+1
m=dec

#Then convert the number into Binary

while m!=0:
    rem=m%8
    octal=octal+str(rem)
    m=m//8
print(octal[::-1])

    
