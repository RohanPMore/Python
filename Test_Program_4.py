def matched(n):
    count=0
    count1=0
    for i in range(len(n)):
        if n[i]=="(":
                count=count+1
        elif n[i]==")":
                 count1=count1+1
        elif count1 > count:
            return 0

    if count==count1:
        return 1
    else:
        return 0
             

a = input('Please enter data using () ')
b = matched(a)
print(b)
