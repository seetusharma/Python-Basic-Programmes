num=int(input("Enter a number: "))
num2=num
rev=0
rem=0
while(num!=0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
if(num2==rev):
    print("Palindrome")
else:
    print("Not palindrome")
    
