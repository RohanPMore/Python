#Counting even and odd in a list
#Creating an empty list
n = int(input('Please provide number of elements in list:  '))
list = []

for i in range(n):
    a = int(input('Enter number:  '))
    list.append(a)

#Defining a function

def counter(list):
    even = 0
    odd = 0
    for j in list:
        if j%2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

E, O = counter(list)

print('Even : ', E, 'Odd : ', O)
            
        
