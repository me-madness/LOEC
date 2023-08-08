dictionaries = {"name": "John",
                "age": 30,
                "city": "New Your",
                "email": "john@example.com"}
# First options
def check_dict(key):
    if key in dictionaries:
        print(key)
    else:
        print(f'this {key} is not exist!') 
        
for key, value in dictionaries.items():
    #Options one
    print(f'{key}: {value}') 
    
    #Options two        
    print(key, ':', value)         
        
check_dict("age", "country")                 
# print(dictionaries)



# second options
var = "age" in dictionaries
if var:
    print("age is present")
else:
    print("age is not present") 

for key, value in dictionaries.items():
    print(f'{key}: {value}')
    print(key, ':', value)                