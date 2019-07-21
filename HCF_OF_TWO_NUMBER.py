num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter second number: "))

i=2
gcd=0
while i<=num1 and i<=num2 and i<=num3:
    if num1%i==0 and num2%i==0 and num3%i==0:
        gcd=i
    i=i+1
print(gcd)
