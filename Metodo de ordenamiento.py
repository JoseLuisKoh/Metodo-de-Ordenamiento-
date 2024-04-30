


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]




arr1 = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr1)
print("Arreglo ordenado usando Burbuja:")
print(arr1)

arr2 = [12, 11, 13, 5, 6]
insertion_sort(arr2)
print("\nArreglo ordenado usando Inserción:")
print(arr2)

arr3 = [64, 25, 12, 22, 11]
selection_sort(arr3)
print("\nArreglo ordenado usando Selección:")
print(arr3)

