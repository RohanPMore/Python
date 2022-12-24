import numpy as np
"""row_size = int(input("Enter row size:  "))
colum_size = int(input("Enter colum size:  "))"""


"""matrix = []         #outer matrix it will include all rows
print("Enter the values row wise: ")

for i in range(row_size):
    a = []          #inner matrix it will include all the column elements 
    for j in range(colum_size):
        a.append(int(input()))  #for elements in the row
    matrix.append(a)            #for rows in the matrix

for a in range(row_size):
    for b in range(colum_size):
        print(matrix[a][b], end = " ")
    print(" ")"""
        
a = np.matrix('110 120; 130 140; 150 160; 170 180; 190 200')
print(a)


