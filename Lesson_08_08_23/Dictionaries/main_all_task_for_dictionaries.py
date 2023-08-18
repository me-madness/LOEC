# # All task for Dictionaries

# # 01. First task Create an empty dictionary

# dictionaries = {}
# dictionaries['name'] = 'John'
# dictionaries['age'] = 35
# dictionaries['city'] = 'New York'
# dictionaries['email'] = 'john@example.com'
# print dictionaries)

# # 2. Second task Access values

# dictionaries = {'name': 'John', 'age': 35, 'city': 'New York', 'email': 'john@example.com'}

# dict1 = dictionaries['name']
# dict2 = dictionaries['email']

# print(f'name: {dict1}')
# print(f'email: {dict2}')
           
# # 3. Third task Check if a key exists

# dictionaries = {"name": "John",
#                 "age": 30,
#                 "city": "New Your",
#                 "email": "john@example.com"}
# # 3.1 First options
# def check_dict(key):
#     if key in dictionaries:
#         print(key)
#     else:
#         print(f'this {key} is not exist!') 
        
# for key, value in dictionaries.items():
#     print(f'{key}: {value}')          
# check_dict("country")                 
# # 3.2 Second options
# var = "age" in dictionaries
# if var:
#     print("age is present")
# else:
#     print("age is not present") 
    
# # 4. Fourth task Iterate over the dictionary

# dictionaries = {"name": "John",
#                 "age": 30,
#                 "city": "New Your",
#                 "email": "john@example.com"}
# # 4.1 First options
# def check_dict(key):
#     if key in dictionaries:
#         print(key)
#     else:
#         print(f'this {key} is not exist!') 
        
# for key, value in dictionaries.items():
#     print(f'{key}: {value}')
# check_dict("country")                      
# # 4.2 Second options
# var = "age" in dictionaries
# if var:
#     print("age is present")
# else:
#     print("age is not present")     
# for key, value in dictionaries.items():
#     print(f'{key}: {value}')
#     print(key, ':', value)
         
# # 5. Fifth task Get the number of key-value pairs

# dictionaries = {"name": "John",
#                 "age": 30,
#                 "city": "New Your",
#                 "email": "john@example.com"}

# for i in range(len(dictionaries)):
#     print(f'List of dictionaries {i}')
#     print('List of dictionaries', i )

# # 6. Sixth task Get a list of all keys

# dictionaries = {"name": "John",
#                 "age": 30,
#                 "city": "New Your",
#                 "email": "john@example.com"}

# list_keys = list(dictionaries.keys())
# # 6.1 First option for printing            
# print(f'List of keys {list_keys}')           
# # 6.2 Second option for printing            
# print("List of values:", list_keys)    


# # 7. Seven task Get a list of all values

# dictionaries = {"name": "John",
#                 "age": 30,
#                 "city": "New Your",
#                 "email": "john@example.com"}

# list_values = list(dictionaries.values()) 
# # 7.1 First option for printing
# print(f'List of values {list_values}')   
# # 7.2 Second option for printing            
# print("List of values:", list_values)                

# # 8. Eighth task  Get a list of key-value pairs

dictionaries = {}

# # 9. Ninth task Update or add new key-value pairs

dictionaries = {}

# # 10. Tenth task Access values

dictionaries = {}

# # 11. Eleventh task Dictionary comprehension 

dictionaries = {}

# # 12. Twelve task Use the pop() 

dictionaries = {}

# # 13. Thirteen task Use the popitem()
dictionaries = {}

# # 14. Fourteen task Use the clear()
dictionaries = {}

# # 15. Fifteen task Use the copy()
dictionaries = {}

# # 16. Sixteen task Use the update()
dictionaries = {}

# # 17. Seventeen task Use the dict()
dictionaries = {}

