#question18:sum of even numbers
n=1234
sum=0
while n>0:
    r=n%10
    if(n%2==0):
      sum=sum+r
    n=n//10
print(sum)