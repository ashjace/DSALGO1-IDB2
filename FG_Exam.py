
x = [1,2,3,4,5]
y = []
z = []

y.append(x.pop())
y.append(x.pop())
z.extend(x)
x.pop()
x.pop()
x.pop()

print("x = ", x)
print("y = ", y)
print("z = ", z)



#2) Insertion Sort Descending Order

X = [1, 2, 21, 33, 45, 65, 12]
arr = []
arr.extend(X)
for i in range(1,len(arr)):
    key=arr[i]
    j = i - 1
    while j >=0 and key > arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
        arr[j + 1] = key

print(arr)

#Selection Sort Ascending Order
X = [1, 2, 21, 33, 45, 65, 12]
arr = []
arr.extend(X)
for i in range(len(arr)):
    min_idx = i
    for j in range(i + 1, len(arr)):
        if arr[min_idx]>arr[j]:
            min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)



