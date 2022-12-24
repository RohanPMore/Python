#Counting particular charachter
string = str(input('Please enter a string:  '))
character = input('Please enter the charachter to be found: ')
count = 0
for i in range(len(string)):
    if string[i] == character:
        count += 1
print('Number of character: ', count)

#Counting spaces
count1 = 0
for j in range(len(string)):
    if string[j] == ' ':
        count1 += 1
print('Number of spaces in string: ', count1)

#Length of string
print('length of string is : ', len(string))
        
                
