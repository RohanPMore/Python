N = int(input())
x = 0
y = []



for i in range(N):
    a = int(input())
    A = input().split()
    b = int(input())
    B = input().split()
    for j in range(a):
        for k in range(b):
            if A[j] == B[k]:
                x += 1
        if x == a:
            y.append('True')
        else:
            y.append('False')
        
for q in range(len(y)):
    print(y[q])
        
    
