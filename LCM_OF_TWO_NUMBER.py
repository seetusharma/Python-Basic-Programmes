num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
greater=max(num1,num2)
lcm=0
while True:
    if greater%num1==0 and greater%num2==0:
        lcm=greater
        break
    greater=greater+1
print(lcm)
