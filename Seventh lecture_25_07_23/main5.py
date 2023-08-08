import sys
import csv

new_file_open_one = 'original_text.txt'
new_file_open_two = 'histogram.txt'
max_value = 10000000000000
new_max_value = ''
histogram = {}


try:
    with open(new_file_open_one, 'r') as file:
        # sys.stdout = file
        reading = file.read()
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
    with open(new_file_open_two, "w") as new_file:
        csv.reader = csv.reader(new_file)
        for key, val in histogram.items():
        #    for num in val:
        #         vals = num.strip().split('\n')  
        #         if vals < max_value:
        #             max_value = vals          
            for val in sorted(histogram.keys()):
                    # print(f"Count of the symbols='{val}' is {histogram[val]}")
                    if val < str(max_value):
                        new_max_value = str(val)               
                        count_two = f"Count of the max value= '{new_max_value}'\n"
                        # " : {key}" + f"Count of the key= '{key}' : {val}"
                        new_file.write(count_two) 
                        print(str(new_max_value)) 
except FileNotFoundError:
    print("File not found!")
finally:       
    new_file.close()
    print(new_file_open_one)               