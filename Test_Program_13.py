r = str(input('Enter a string: '))
count = 0
count1 = 0
for i in range(len(r) + 1):
    if r[i] == '.':
        count += 1
    if r[i] == '.' and r[i+1] == '':
        count1 += 1

if count > 1 or count1 >= 1:
    print('False')
else:
    print('True')
