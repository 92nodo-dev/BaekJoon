n, m = map(int, input().split())

arr1 = []
arr2 = []

for i in range(n) :
    tmp = input().split()
    for t in tmp :
        arr1.append(int(t))
for i in range(n) :
    tmp = input().split()
    for t in tmp :
        arr2.append(int(t))
for i in range(n*m) :
    arr1[i] += arr2[i]
    
for i in range(n) :
    for j in range(m) :
        print(str(arr1[i*m+j]), end=" ")
    print()
