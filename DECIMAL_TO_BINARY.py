num=int(input("Enter a decimal number: "))
rem=0
binary=""
while num!=0:
    rem=num%2
    binary=binary+str(rem)
    num=num//2  
print(binary[::-1])
    
