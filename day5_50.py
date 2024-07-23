#reverse the numbers present in a given string
str=1234
rev=" "
while str>0:
    r=str%10
    rev=rev+str(rev)
    str=str//10
print(str(rev))