#question16:sum of digits
n=123
sum=0
while n>0:
    r=n%10
    sum=sum+r  #important line
    n=n//10
print(sum)