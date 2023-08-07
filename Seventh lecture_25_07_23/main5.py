new_file_open = 'histogram.txt'
new_file_open_two = 'original_text.txt'
message = "File not found!"
vals = ''
vals_one = ''

try:
    with open(new_file_open_two, 'r') as file:
    reading = file.read()
    histogram = {}
except FileNotFoundError:
    print(message) 
    

try:
    for x in reading:
        if x in histogram:
            histogram[x] = histogram[x] + 1
        else:
            histogram[x] = 1
except FileNotFoundError:
    print(message)
finally:            
    file.close()   

try:
    with open(new_file_open, "w") as new_file:
        for key, val in histogram.items():
           for vals in val: 
                vals += val
                if val > vals:
                    vals_one += val 
                    count_two = f"Count of the value= '{vals_one}' : {key}" + f"Count of the key= '{key}' : {val}\n"
        # count = f"Count of the key= '{key}' : {val}\n"
        # new_file.write(count) 
except FileNotFoundError:
    print("File not found!")
finally:
        
    new_file.write(count_two) 
    new_file.close()
    print(new_file_open)       
# for val in sorted(histogram.keys()):
#     print(f"Count of the symbols='{val}' is {histogram[val]}")        