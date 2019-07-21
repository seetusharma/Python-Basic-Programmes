num1=int(input("enter starting range "))
num2=int(input("enter ending range "))
for i in range(num1,num2+1):
    for j in range(2,i//2):
        if i%j==0:
            print("*",end=",")
            break
    else:
        print(i,end=",")
        
