#Consider the given input and output:

#Input: Get 3 strings in 3 lines as input

#Hello
#Hi
#Good Morning

#Output:

#In the 1st string, replace the vowels with “
#In the 2nd string, replace the consonants with *
#In the third string, convert the lowercase letters to upper case.

str1=input() 
str2=input() 
str3=input() 

for i in range(len(str1)):
    if str1[i]=='a' or str1[i]=='e' or str1[i]=='i' or str1[i]=='o' or str1[i]=='u' or str1[i]=='A' or str1[i]=='E' or str1[i]=='I' or str1[i]=='O' or str1[i]=='U':
        str1=str1.replace(str1[i],'"')
print(str1)

for i in range(len(str2)):
    if str2[i]=='a' or str2[i]=='e' or str2[i]=='i' or str2[i]=='o' or str2[i]=='u' or str2[i]=='A' or str2[i]=='E' or str2[i]=='I' or str2[i]=='O' or str2[i]=='U':
        str2=str2.replace(str2[i],'*')
print(str2)

print(str3.upper())


