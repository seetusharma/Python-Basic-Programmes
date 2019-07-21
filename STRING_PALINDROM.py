str_in=input("Enter a word: ")
print("Before reverce:",str_in)
print("After reverce:",str_in[::-1])
if(str_in==str_in[::-1]):
    print("Palindrom")
else:
    print("Not Palindrom")
