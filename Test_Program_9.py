nikita = [8,8,0,2,0,4,4,8,8]
patil = {}
for a in nikita:
    if a in patil:
        patil[a] = patil[a] + 1
    else:
        patil[a] = 1

print(patil)
max_key = max(patil, key=patil.get)
min_key = min(patil, key=patil.get)
print(max_key, min_key)
