#write a program to print all the vowels followed by consonants
vowels="aeiou"
consonant="bcdfghjklmnpqrstvwxy"
i="hello wOrld"
inp=i.lower()
for i in inp:
    if(i in vowels):
        print(i,end='')
for i in inp:
    if(i in consonant):
      print(i,end='')