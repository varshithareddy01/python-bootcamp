#print the unique characters in a string
str=input()
for i in str:
    count=str.count(i)
    if count==1:
        print(i,end='')