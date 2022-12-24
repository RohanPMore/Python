if __name__ == '__main__':
    N = int(input())
    output = []
    j = 0
    while(j <= N):
        usr_input = input().split(' ')
        if len(usr_input) == 3:
            x, y, z = usr_input[0].strip(), int(usr_input[1]), int(usr_input[2])
            if x == 'insert':
                output.insert(y, z)
                j += 1
            
        elif len(usr_input)==2:
            x,y = usr_input[0].strip(), int(usr_input[1])
            if x == 'append':
               output.append(y)
               j += 1
            elif x == 'remove':
                output.remove(y)
                j += 1
        else:
            x = usr_input[0].strip()
            if x == 'pop':
                output.pop()
                j += 1
            elif x == 'sort':
                output.sort()
                j += 1
            elif x == 'reverse':
                output.reverse()
                j += 1
            elif x == 'print':
                j += 1
                print(output)
            

    
        
        
        
    
