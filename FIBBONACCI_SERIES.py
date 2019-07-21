num=int(input("Enter the nth term of the series: "))
if num>0:
    n1=0
    n2=1
    
    for i in range(1,num+1):
        print(i,"term of series:   ",n1)
        nth=n1+n2
        n1=n2
        n2=nth
        
else:
    print("Enter a number greater then zero")
