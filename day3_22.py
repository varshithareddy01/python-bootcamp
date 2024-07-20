# replace the elements in an arrays with average of maximum and minimum elements in elements
#sample 
my_list=list(map(int,input().split()))
mini=my_list[0]
maxi=my_list[0]
sum=0
for i in range(len(my_list)):
    if(my_list[i]<mini):
        mini=my_list[i]
    print(mini)
else:
    maxi=my_list[i]
    print(maxi)
avg=(mini+maxi)//2
for i in range(len,(my_list)):
    my_list[i]=avg
print(my_list)

