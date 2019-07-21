num=int(input("Enter a decimal number"))
rem=0
dec=""
while num!=0:
    rem=num%8
    dec=dec+str(rem)
    num=num//10
print(dec[::-1])
