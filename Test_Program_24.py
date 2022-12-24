print("          ***************************************")
print("               Created by: Rohan Promod More")
print("          ***************************************")
print("")

n = int(input("Enter Pattern size: "))
print("")

for rows in range(1, n+1):          #helps to get row range 1,2,3,4,5
    for columns in range(1, n+1):   #helps to get column range 1,2,3,4,5
        if(columns <= n and columns >= ((n+1) - rows)):
            print("*", end="")   #for printing on same line
        else:
            print(" ", end="")
    print("\r")                    #get to new line after inside for loop is completed

