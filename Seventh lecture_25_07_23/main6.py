file = open('original_text.txt', 'r')
reading = file.read()
reading = reading.replace('castle', 'palace')
count_reading = reading.count('castle')
print(f"the word 'castle' was replaced by word 'palace' {count_reading} times")
file.close()
new_file_open = 'modified_text.txt'
new_file = open(new_file_open, 'w')
new_file.write(reading)
new_file.close()
print(reading)


