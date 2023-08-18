dict1 = {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'David': 92}

# # 11.1 First option
dict2 = {}
for k,v in dict1.items():
    dict2[k] = v / 100
print(dict2)    
# # 11.2 Second option
dict3 = {k: v / 100 for k,v in dict1.items()}
print(dict3)