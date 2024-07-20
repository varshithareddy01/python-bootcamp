my_list=list(map(str,input().split(",")))
choice=int(input())
print("enter the choice\n 1.append\n 2.pop\n 3.sort\n 4.len\n")
if(choice==1):
    my_list.append(9999)
    print(my_list)
elif(choice==2):
    my_list.pop(3)
    print("my_list")
elif(choice==3):
    my_list.sort()
    print("my_list")
else:
    print(len(my_list))



