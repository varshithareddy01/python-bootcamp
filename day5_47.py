#write a program to print all the consonants and vowels
vowels="aeiou"
consonant="bcdfghjklmnpqrstvwxy"
count=0
c=0
i="hello wOrld"
inp=i.lower()
for i in inp:
    if(i in vowels):
        count+=1
for i in inp:
    if(i in consonant):
         c+=1
print(c)