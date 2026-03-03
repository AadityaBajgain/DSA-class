def selection_Sort(arr, low):
    if low == len(arr):
        return
    

    min_index = low

    for i in range(low+1, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
        
    arr[min_index], arr[low] = arr[low], arr[min_index]

    selection_Sort(arr, low+1)
    

arr = [5,3,6,7,9,33,2,8]
selection_Sort(arr,0)
print(arr)