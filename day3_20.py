#question11: find the maximum element in a given list
#test code=0
#12 23 36 44 45 57
#o/p:57
#test case1=0
#56 78 -8 12 34 -99
#o/p:78
my_list=list(map(int,input().split()))
maxi=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>maxi):
        maxi=my_list[i]
print(maxi)