'''''
#Insertion Sort
arr1 = [10,2,3,1,1,4,89,21]
print(arr1)
print("Insertion sort")'''''
def InsertionSortAscending(arr1):
    for i in range(1, len(arr1)):
        key = arr1[i]
        j = i - 1
        while j >= 0 and key < arr1[j]:
            arr1[j + 1] = arr1[j]
            j -= 1
        arr1[j + 1] = key

def InsertionSortDescending(arr1):
    for i in range(1, len(arr1)):
        key = arr1[i]
        j = i - 1
        while j >= 0 and key > arr1[j]:
            arr1[j + 1] = arr1[j]
            j -= 1
        arr1[j + 1] = key
'''''
print("After Insertion Sort")
InsertionSort(arr1)
print(arr1)

#Selection Sort

print("Selection sort")
arr2 = [10,2,3,1,1,4,89,21]'''''

def SelectionSortAscending(arr2):
    for i in range(len(arr2)):
        min_idx = i
        for j in range(i + 1, len(arr2)):
            if arr2[min_idx] > arr2[j]:
                min_idx = j
        arr2[i], arr2[min_idx] = arr2[min_idx], arr2[i]

def SelectionSortDescending(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] < arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

'''''
print("After Selection Sort")
SelectionSort(arr2)
print(arr2)

#Bubble Sort

arr3 = [10,2,3,1,1,4,89,21]'''''

def BubbleSort(arr3):
    for i in range(len(arr3)):
        for j in range(0, len(arr3) - i - 1):
            if arr3[j] > arr3[j + 1]:
                arr3[j], arr3[j + 1] = arr3[j + 1], arr3[j]
'''''                
print("After Bubble Sort")
BubbleSort(arr3)
print(arr3)'''''



#1.[23,89, 7, 56, 44] – Implement the Bubble Sort Algorithm for the Dataset and
#sort the data into ascending order.
num1=[23,89,7,56,44]
print("Number 1. Array before the Bubble Sort")
print(num1)
BubbleSort(num1)
print("Number 1. Array after the Bubble Sort")
print(num1)


#2.[12, 78, 91, 34, 62] – Implement the
#Insertion Sort Algorithm for the Dataset and sort the data into ascending order.
num2 = [12, 78, 91, 34, 62]
print("\nNumber 2. Array before the Selection Sort")
print(num2)
SelectionSortAscending(num2)
print("Number 2. Array after the Selection Sort")
print(num2)

#3.[5, 99, 48, 15, 67] – Implement the
#Selection Sort Algorithm for the Dataset and sort the data into descending order.
num3 = [5, 99, 48, 15, 67]
print("\nNumber 3. Array before the Selection Sort")
print(num3)
SelectionSortDescending(num3)
print("Number 3. Array after the Selection Sort")
print(num3)

#4.[38, 82, 25, 74, 13] – Implement the
#Insertion Sort Algorithm for the Dataset and sort the data into descending order.
num4 = [38, 82, 25, 74, 13]
print("\nNumber 4. Array before the Insertion Sort")
print(num4)
InsertionSortDescending(num4)
print("Number 4. Array after the Insertion Sort")
print(num4)

#5.Copy all of the values from the
#second index and third index of the previous datasets into one
#dataset. After copying, sort the data into ascending order and descending
#order each order of the dataset is inserted into a separate list/array.
num5= [44,56,62,78,48,15,38,25]
print("\nNumber 5. Array before Sorting (Insertion Sort)")
print(num5)
print("Number 5. Array after the Ascending Sort")
InsertionSortAscending(num5)
num5Ascended = num5
print(num5Ascended)
print("Number 5. Array after the Descending Sort")
InsertionSortDescending(num5)
num5Descended = num5
print(num5Descended)

#6.Create a new list/array or values copying all of
#the values from item number 1 to 4. Implement the Selection
#Sort Algorithm and sort the data into ascending order.
num6= [23, 89, 7, 56, 44,12, 78, 91, 34, 62,5, 99, 48, 15, 67,38, 82, 25, 74, 13]
print("\nNumber 6. Array before the Selection Sort")
print(num6)
SelectionSortAscending(num6)
print("Number 6. Array after the Selection Sort")
print(num6)

#7.Print the even and odd values of the
#list/array created in item number 6.
num7odd = [23, 89, 7, 91, 5, 99, 15, 67, 25, 13 ]
num7even = [56, 44, 12, 78, 34, 62, 48, 38, 82, 74]
print("\nNumber 7 . Odd Numbers :", num7odd)
print("Number 7. Even Numbers :", num7even)
