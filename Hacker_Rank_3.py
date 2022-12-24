n = int(input())
list = []
for i in range(n):
    number = int(input('Enter Number:  '))
    list.append(number)
    i+=1
print(list)

list.sort()

print(list[-2])
