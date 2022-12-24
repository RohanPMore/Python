def count_substring(string, sub_string):
    sum = 0
    m = len(string)-(len(sub_string)-1)
    for i in range(m):
        if string.count(sub_string,i,i+len(sub_string)):
            sum = sum + 1
    return sum

if __name__ == '__main__':
    string = input()
    sub_string = input()
    print(count_substring(string, sub_string))

string = input()
sub_string = input()

m = len(string) - (len(sub_string)-1)

for i in range(0, m):
    x = 0
    count = 0
    for j in range(0, len(sub_string)):
        if string.count(sub_string,j,j+len(sub_string)):
            count = count + 1

print(count)
                
    
