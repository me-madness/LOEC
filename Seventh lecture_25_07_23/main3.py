file = open('original_text.txt', 'r')
reading = file.read()
histogram = {}
for x in reading:
    if x in histogram:
        histogram[x] = histogram[x] + 1
    else:
        histogram[x] = 1
file.close()
print(histogram)

for key, val in histogram.items():
    print(f"count of the symbols='{key}' is {val}")
    
print(histogram.keys())    
print(histogram.values())    

for key in sorted(histogram.keys()):
    print(f"Count of the symbols='{key}' is {histogram[key]}")
    
    



# file = open('original_text.txt', 'r')
# reading = file.read()
# dict = {}
# s = set(reading)
# file.close()   