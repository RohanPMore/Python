def checkstringstruct(s):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    for i in range(len(s)):
        if s[i].isalpha():
            count1 = count1 +1
    for j in range(len(s)):
        if s[j].isdigit():
            count2 = count2 +1
    for k in range(len(s)):
        if s[k].islower():
            count3 = count3 +1
    for l in range(len(s)):
        if s[l].isupper():
            count4 = count4 +1
    if count1 >= 1 and count2 >=1:
        a = print("True")
    else:
        a = print("False")
    if count1 >= 1:
        b = print("True")
    else:
        b = print("False")
    if count2 >= 1:
        c = print("True")
    else:
        c = print("False")
    if count3 >= 1:
        d = print("True")
    else:
        d = print("False")
    if count4 >= 1:
        e = print("True")
    else:
        e = print("False")
    return a; b; c; d; e
            

s= input()
checkstringstruct(s)
    
        
