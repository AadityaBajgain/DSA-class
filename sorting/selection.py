def selection_sort(arr,n):
    for i in range(0,n-1):
        j = k = i
        for j in range (i,n):
            if arr[k] > arr[j]:
                k = j
        arr[k], arr[i] = arr[i], arr[k]


arr = [8,5,7,3,2] 
selection_sort(arr, len(arr))
print(arr)