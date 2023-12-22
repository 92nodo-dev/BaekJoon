arr = [1,1,2,2,2,8]
tmp = input().split()
for i in range(len(arr)) :
    print(str(arr[i]-int(tmp[i])), end=" ")
