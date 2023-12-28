x = 0
y = 0
maxValue = -1
for i in range(9) :
    arr = input().split()
    for j in range(len(arr)) :
        if maxValue < int(arr[j]) :
            maxValue = int(arr[j])
            x = i+1
            y = j+1

print(maxValue)
print(str(x) + " " + str(y))

