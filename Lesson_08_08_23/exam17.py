mylist = ('a', 1), ('b', 2), ('c', 3) 

mydict = dict(mylist)
print(mydict)

mydict ={key: value for key, value in mylist}
print(mydict)