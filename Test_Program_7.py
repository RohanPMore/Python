print("Enter a list")
n = int(input('Enter number of elements in list:  '))
list = []
for i in range(n):
        a = int(input('Enter numbers in list:  '))
        list.append(a)
#list.sort()
for j in range(len(list)):
    for k in range(j+1,len(list)):
        if list[j]>list[k]:
            list[j],list[k] = list[k],list[j]
print(list)
list1 = []
count1 = 0
for x in range(len(list)):
    for y in range(x+1,len(list)):
        if list[x] == list[y]:
            count1 += 1
if count1 == 2:
    b = list[x]
    list1.append(b)
print(list1)
                

            
