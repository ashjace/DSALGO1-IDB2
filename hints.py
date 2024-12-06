for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
        if arr[min_idx]<arr[j]:
            mind_idx=j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

for i in range(1,len(arr)):
    key=arr[i]
    j = i-1
    while j >=0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
        arr[j + 1]
