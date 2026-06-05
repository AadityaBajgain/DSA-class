def bubble_sort(arr, n):
    for i in range(n-1):
        flag = 0
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1
        if flag == 0:
            return "array is already sorted"


arr = [8,5,7,3,2]
bubble_sort(arr, len(arr))
print(arr)



def bubble(arr, n):
    for i in range(n-1):
        flag = 0
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                flag = 1
        if flag == 0:
            break
        