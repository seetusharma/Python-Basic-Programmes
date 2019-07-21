#WAP to find the extension of any file.

str1=input("Enter a file name with its extension")
for i in range(len(str1)):
    if str1[i]=='.':
        break
print(str1[i+1:])
