file = open('original_text.txt', 'r')
reading = file.read()
dict = {}
s = set(reading)
for i in s:
    dict[i] = ''
    print(dict)
file.close()