arr = []

for i in range(3) :
    arr.append(int(input()))

for i in range(1, 6) :
    if i in arr :
        continue
    print(str(i), end=" ")
