x = "BRENDAN ABDUL JAKOL D. SALSALANI TEENAGERLOVER"
print(x)

'''' make an insertion loop array'''
arr = [5,4,8,7,6,9,2,1,3,10]
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
print(arr)


arr1 = [15,14,18,17,16,19,12,11,13,20]
for i in range (len(arr1)):
    min_index = i
    for j in range( i + 1, len(arr1)):
        if arr1[min_index] > arr1[j]:
            min_index = j
    arr1[i], arr1[min_index] = arr1[min_index], arr1[i]
print(arr1)

arr3 = [22,23,27,29,24,25,21,26,28,30]
for i in range(len(arr3)):
    for j in range (0, len(arr3)- i - 1):
        if arr3[j] > arr3[j +1]:
            arr3[j], arr3[j+1] = arr3[j+1], arr3[j]
print(arr3)
