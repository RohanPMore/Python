n = int(input('Please enter number:  '))
while 1 <= n <= 100:
    if n%2 != 0:
        print('Weird')
    elif n%2 == 0 and 2 <= n <= 5:
        print('Not Weird')
    elif n%2 == 0 and 6 <= n <=20:
        print('Weird')
    elif n%2 == 0 and n > 20:
        print('Not Weird')
else:
    print('Incorrect input')
