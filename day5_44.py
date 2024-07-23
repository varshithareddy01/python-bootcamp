check=['a','e','i','o','u']
count=0
inp="hello world"
for i in inp:
    if(i in check):
        count+=1
print(count)