my_list = [1, 2, 2, 3, 4, 3, 5, 6, 6, 6, 1]


    
for x in my_list:
    if my_list.count(x) > 1:
        my_list.remove(x)
print*(my_list)            
          
for i in range(min(my_list), max(my_list)+1):          
    # remove_number(i)

list1 = [1, 2, 3]
list2 = list1.copy()
list1[0] = 11
print(list1)
print(list2)