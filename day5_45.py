check=['a','e','i','o','u']
count=0
i="hello world"
inp=i.lower()
for i in inp:
    if(i in check):
        count+=1
print(count)