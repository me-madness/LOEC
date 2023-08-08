list1 = [1,2,2,3,4,3,5,6,6,1]
unique_list = []
for element in list1:
    if element not in unique_list:
        unique_list.append(element)

unique_list = [element for element in list1 if element not in unique_list]