def split_and_join(line):
    # write your code here
    modifiedLine = line.split(" ")
    modifiedLine = "-".join(modifiedLine)

    return modifiedLine 

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
