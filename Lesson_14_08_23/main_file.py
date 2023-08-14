from numpy import array
import numpy as np

table_one_list = [[6, 4, 3, 2],
                  [3, 4, 5, 6]]

table_two_list = [[6, 4, 3, 2],
                  [3, 4, 5, 6]]

table_three_list = []

for row1 in range(len(table_one_list)):
    temp_list = []
    for row2 in range(len(table_one_list[0])):
        table_three_list.append(table_one_list[row1][row2] + table_two_list[row1][row2])
    table_three_list.append(temp_list)
print(table_three_list)


table_one_list_numpy = array(table_one_list)    