
#1) Bubble Sort
arr1 = [23, 89, 7, 56, 44]
print("\nArr1 values before Bubble Sort")
print(arr1)
for i in range(len(arr1)):
    for j in range(0, len(arr1) - i - 1):
        if arr1[j] > arr1[j + 1]:
             arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]
print("Array 1 values after Bubble Sort Ascending")
print(arr1)


#2) Insertion Sort
arr2 = [12, 78, 91, 34, 62]
print("\nArr2 before Insertion Sort")
print(arr2)
for i in range (len(arr2)):
    key = arr2[i]
    j = i - 1

    while j >= 0 and key < arr2[j]:
        arr2[j + 1] = arr2[j]
        j -= 1
    arr2[j + 1] = key
print("Arr2 after Insertion Sort Ascending")
print(arr2)

#3) Selection Sort
arr3 = [5, 99, 48, 15, 67]
print("\nArr3 before Selection Sort")
print(arr3)

for i in range(len(arr3)):
    max_idx = i
    for j in range(i + 1, len(arr3)):
        if arr3[max_idx] < arr3[j]:
            max_idx = j

    arr3[i], arr3[max_idx] = arr3[max_idx], arr3[i]  #

print("Arr3 values after Selection Sort Descending")
print(arr3)

#4) Insertion
arr4 =  [38, 82, 25, 74, 13]
print("\nArr4 before Insertion Sort")
print(arr4)
for i in range(len(arr4)):
    key = arr4[i]
    j = i - 1
    while j >= 0 and key > arr4[j]:
        arr4[j + 1] = arr4[j]
        j -= 1
    arr4[j + 1] = key
print("Arr4 after Insertion Sort Descending")
print(arr4)


#5)

arr5 = [23, 44, 34, 62 , 67, 48, 74, 38]
print("\nArr5 before Insertion Sort")
print(arr5)
for i in range(len(arr5)):
    key = arr5[i]
    j = i - 1
    while j >= 0 and key < arr5[j]:
        arr5[j + 1] = arr5[j]
        j -= 1
    arr5[j + 1] = key
print("Arr5 after Insertion Sort Ascending")
print(arr5)

arr6 = [23, 44, 34, 62 , 67, 48, 74, 38]
print("\nArr6 before Insertion Sort")
print(arr6)
for i in range(len(arr6)):
    key = arr6[i]
    j = i - 1
    while j >= 0 and key > arr6[j]:
        arr6[j + 1] = arr6[j]
        j -= 1
    arr6[j + 1] = key
print("Arr6 after Insertion Sort Descending")
print(arr6)

#6)

arr7 =  [23,89, 7, 56, 44, 12, 78, 91, 34, 62, 5, 99, 48, 15, 67, 38, 82, 25, 74, 13]
print("\nArr7 before Selection Sort")
print(arr7)
for i in range(len(arr7)):
    min_idx = i
    for j in range(i + 1, len(arr7)):
        if arr7[min_idx] > arr7[j]:
            min_idx = j
    arr7[i], arr7[min_idx] = arr7[min_idx], arr7[i]
print("Arr7 values after Selection Sort")
print(arr7)
arr7 = [23, 89, 7, 56, 44, 12, 78, 91, 34, 62, 5, 99, 48, 15, 67, 38, 82, 25, 74, 13]
#Even
even_numbers = [number for number in arr7 if number % 2 == 0]
#Odd
odd_numbers = [number for number in arr7 if number % 2 != 0]
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
