# First task create List

# empty_list = [3, 'words', 33, 2.5]
# empty_list = []
# empty_list.append(3)
# empty_list.append('words')
# empty_list.extend([33, 2.5])
# print(empty_list)

# Second task Access to the List

# empty_list = [4, 5, 21, 2.15, 2, 2.5, 7, 11]
# print(empty_list[1])
# print(empty_list[-3])


# Third task slice to the List

# empty_list = [5, 4, 1.1, 1.5, 1.7, 13, 4, 6]
# print(empty_list[1:(-3+1)])
# print(empty_list[1:5])
# print(empty_list[:5:2])
# print(empty_list[2::2])
# empty_list = empty_list.slice(-3, 6, -1)

# Fourth task Iterate to the list

# First option
empty_list = [5, 4, 1.1, 1.5, 1.7, 13, 4, 6]
for i in empty_list:
    print(f"{i} is the list element")
    print(i, "is the list element")
# Second option    
for i in range(8):    
    print(empty_list[i], "is the list element")
    
    
# Fifth find the length to the LIst  

empty_list = [5, 4, 1.1, 1.5, 1.7, 13, 4, 6]