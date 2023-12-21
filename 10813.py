a,b = map(int, input().split())
bask = []
for i in range(a+1) :
    bask.append(i)

for _ in range(b) :
    x,y = map(int, input().split())
    z = bask[x]
    bask[x] = bask[y]
    bask[y] = z

for i in range(1, a+1) :
    print(bask[i], end=" ")
    
