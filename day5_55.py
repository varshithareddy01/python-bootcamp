#select one aplhabet and from next skip 4 aplhabets and print the next alphabet in capital letters
t=input()
n=int(input())
for i in t:
    print(chr(ord(i)+n))