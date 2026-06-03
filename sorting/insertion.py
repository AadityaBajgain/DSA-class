def insertion_sort(arr, n):
    for i in range(1, n):
        x = arr[i]
        j = i - 1
        
        while (j > -1 and arr[j] > x):
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = x
        


arr = [8,5,7,3,2]
print(arr)
insertion_sort(arr,len(arr))
print(arr)