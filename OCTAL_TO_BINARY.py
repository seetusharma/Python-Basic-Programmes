num=int(input("Enter a number in Octal: "))
rem=0
dec=0
i=0

# First convert the number into decimal

while num!=0:
    rem=num%10
    dec=dec+rem*pow(8,i)
    num=num//10
    i=i+1
m=dec

# Then convert the number into Binary

bi=""
while m!=0:
    rem=m%2
    bi=bi+str(rem)
    m=m//2
print(bi[::-1])
    

