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
    
list_keys = list(dictionaries.keys())            
list_values = list(dictionaries.values()) 

# List one printing
print(f'List of keys {list_keys}')           
print(f'List of values {list_values}')   


#list two printing
print("List of keys:", list_keys)           
print("List of values:", list_values)         
       
check_dict("country")                 



# second options
var = "age" in dictionaries
if var:
    print("age is present")
else:
    print("age is not present") 

for key, value in dictionaries.items():
    print(f'{key}: {value}')
    print(key, ':', value)                