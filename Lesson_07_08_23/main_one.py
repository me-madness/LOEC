# 1. First task create List

# empty_list = [3, 'words', 33, 2.5]
# empty_list = []
# empty_list.append(3)
# empty_list.append('words')
# empty_list.extend([33, 2.5])
# print(empty_list)

# 2. Second task Access to the List

# empty_list = [4, 5, 21, 2.15, 2, 2.5, 7, 11]
# print(empty_list[1])
# print(empty_list[-3])


# 3. Third task slice to the List

# empty_list = [5, 4, 1.1, 1.5, 1.7, 13, 4, 6]
# print(empty_list[1:(-3+1)])
# print(empty_list[1:5])
# print(empty_list[:5:2])
# print(empty_list[2::2])
# empty_list = empty_list.slice(-3, 6, -1)

# 4. Fourth task Iterate to the list

# # First option
# empty_list = [5, 4, 1.1, 1.5, 1.7, 13, 4, 6]
# for i in empty_list:
#     print(f"{i} is the list element")
#     print(i, "is the list element")
# # Second option    
# for i in range(8):    
#     print(empty_list[i], "is the list element")
    
    
# 5. Fifth task find the length to the LIst  

# # 5.1 First way
# empty_list = [5, 4, 1.1, 1.5, 1.7, 13, 4, 6]
# len(empty_list)
# print(empty_list)
# print(empty_list.len())
# # 5.2 Second Way
# for i in range(len(empty_list)):    
#      print(f"{i} is the list element")
#      print(i, "is the list element")    
# # 5.3 Third Way     
# length = 0
# for _ in empty_list:
#          length += 1
# print(length) 

# 6. Sixth task check if an element exists 

empty_list = [1, 3, 5, 8, 6]
# # 6.1 First Way
# print("Please, enter a number")
# try:
#     a = int(input()) 
#     if a in empty_list:
#         print(a, "exists")
#     else:
#         print(a, "Does not exist")     
# except:   
#     print('Your input is not correct')    
# 6.2 Second Way    
print("Please, enter a number")
while True:
    try:
        a = int(input()) 
        break   
    except:
        print('Your input is not correct')  


if a in empty_list:
    print(a, "exists")
else:
    print(a, "Does not exist")              
    
# 7. Seven task count the occurrences 

# empty_list = [1, 3, 5, 1, 3, 5, 8, 4, 3, 5, 1, 3, 5, 8, 6, 5, 8, 6 ]
# empty_list.count()   

# # 8. Eighth task find the index 

# empty_list = [1, 3, 5, 8, 6, 5, 6, 2, 5]
# empty_list.index()

# # 9. Ninth task  reverse the order

# empty_list = [1, 3, 5, 8, 6, 5, 6, 2, 5]
# empty_list.reverse()

# # 10. Tenth task sort the list

# empty_list = [1, 3, 5, 8, 6, 9, 0]
# empty_list.sort()

# # 11. Eleventh task remove elements

# empty_list = [1, 3, 5, 8, 6, 9, 0]
# empty_list.remove()
# empty_list.pop()

# # 12. Twelve task  clear all elements

# empty_list = [1, 3, 5, 8, 6, 9, 0 ]
# empty_list.clear()

# # 13. Thirteen task  create a copy of the list 

# empty_list_two = 0
# empty_list_two.copy(empty_list)
# empty_list = []

# # 14. Fourteen task concatenate two lists 

# empty_list_one = [1, 3, 5, 8, 6, 9, 0]
# empty_list_two = [ 6, 9, 2, 10]


# # 15. Fifteen task use list comprehension

# empty_list = [1, 3, 5, 8, 6, 9, 0 ]
# squares[empty_list]

# # 16. Sixteen task combine two lists

# empty_list_one = [1, 2, 3]
# empty_list_two = ['a', 'b', 'c']
# zip()

# # 17. Seventeen task find the maximum and minimum elements  

# empty_list = [1, 3, 5, 8, 6, 9, 0 ]
# max()
# min()

# # 18. Eighteen task calculate the sum

# empty_list = [1, 3, 5, 8, 6, 9, 0]
# sum()

# # 19. Nineteen task use the enumerate()

# empty_list = [1, 3, 5, 8, 6, 9, 0]
# enumerate()

# # 20. Twenty task use list unpacking 

# empty_list = [1, 3, 5, 8]

# # 21. Twenty-one task remove duplicate elements 

# empty_list = [1, 2, 2, 3, 4, 3, 5, 6, 6, 1]
# empty_list.remove()   
    