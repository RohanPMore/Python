numberofItems = int(input())
x = []

y, z = input().split()
x.append(y)
x.append(z)

FirstTuple = tuple(x)

print(hash(FirstTuple))
