def binary_search(arr, key , low, high):

    mid = int(( high+low )/ 2)
    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binary_search(arr, key, mid+1, high)
    if key < arr[mid]:
        return binary_search(arr, key, low, mid-1)

arr = [1,3,4,6,7,9,12]

print(binary_search(arr, 3, 0, len(arr)-1))
