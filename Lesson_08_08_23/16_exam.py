list1 = ['', '', '']
list2 = ['a', 'b', 'c']
list3 = ['1a', '1b', '1c']
list4 = ['2a', '2b', '2c']
combined_list = zip(list1, list2, list3, list4)
print(type(combined_list))
print(list(combined_list))