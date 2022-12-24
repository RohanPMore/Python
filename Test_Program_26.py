print("          ***************************************")
print("               Created by: Rohan Promod More")
print("          ***************************************")
print("")

r = int(input("Enter pattern size: "))
#c = int(input("Enter column size: "))
print("")

for rows in range(1, r+1): #helps to get row range 1,2,3,4,5
    k=0
    for columns in range(1, r+1):   #helps to get column range 1,2,3,4,5
        if(5-rows <= columns <= rows +3 and rows-3 <= columns <= 11-rows):
            if(k==1):
                print(" ", end="")   #for printing on same line
                k=0
            else:
                print("*", end="")
                k=1
                
        else:
            print(" ", end="")
            
    print("\r")                    #get to new line after inside for loop is completed
