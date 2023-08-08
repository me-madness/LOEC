list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = ['1a', '1b', '1c']
list4 = ['2a', '2b', '2c']
combined_list = zip(list1, list2)
numbered_list = enumerate(list1)
print(list(combined_list))
print(list(numbered_list))


new_list = [temp_tuple for temp_tuple in combined_list]
print(new_list)


# first way
for el in list:
    print(f'at index {ind} element is {el}')
    ind = ind + 1

# second way
for ind, el in enumerate(list):
    print(f'at index {ind} element is {el}')


# this is true
for temp_tuple in combined_list:
    print(temp_tuple)
    
#the bold are true
print(", ".join(temp_tuple for temp_tuple in combined_list))