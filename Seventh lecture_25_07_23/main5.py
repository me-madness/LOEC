# import sys

new_file_open = 'histogram.txt'
new_file_open_two = 'original_text.txt'
max_value = 10000000000000


try:
    with open(new_file_open_two, 'r') as file:
        # sys.stdout = file
        reading = file.read()
        histogram = {}
        for x in reading:
            if x in histogram:
                histogram[x] = histogram[x] + 1
            else:
                histogram[x] = 1
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # sys.stdout = sys.__stdout__    
    file.close()   
    
    
try:
    with open(new_file_open, "w") as new_file:
        for key, val in histogram.items():
           for i in range[val]:
                vals = i[val]   
                if vals < max_value:
                    max_value = vals
                     
            # for val in sorted(histogram.keys()):
            #     print(f"Count of the symbols='{val}' is {histogram[val]}")                
                    
                    count_two = f"Count of the value= '{vals}' : {key}" + f"Count of the key= '{key}' : {val}\n"
                    new_file.write(count_two) 
                print(str(max_value)) 
except FileNotFoundError:
    print("File not found!")
finally:       
    new_file.close()
    print(new_file_open)               