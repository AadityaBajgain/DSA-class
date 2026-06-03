def quick_sort(arr, l, h):
    if l<h:
        j = partition(arr,l,h)
        quick_sort(arr,l,j-1)
        quick_sort(arr,j+1,h)
        

def partition(arr, low, high):
    pivot = arr[low]

    i = low + 1
    j = high

    while True:

        while i <= high and arr[i] <= pivot:
            i += 1

        while j >= low and arr[j] > pivot:
            j -= 1

        if i > j:
            break
        
        arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]

    return j

arr = [8,5,7,3,2] 
quick_sort(arr, 0,len(arr)-1)
print(arr)