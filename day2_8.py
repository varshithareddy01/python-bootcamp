#program adding my list to new list
my_list=[1,2,3,4]
my_list.append(9999)
my_list.insert(8000,999)
print(len(my_list))
my_list.pop(2)
my_list_2=[5,6,7,8]
new_list=my_list+my_list_2
print(*new_list)
