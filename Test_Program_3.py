number = input('Enter any non-single digit number ')
def intreverse(number):
    endmsg = ""
    for i in range(1, 1+len(number)):
     endmsg = endmsg + number[-i]
    return endmsg
a = intreverse(number)
print(a)







