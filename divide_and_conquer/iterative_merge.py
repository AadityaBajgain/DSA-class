def merge(arr, l, mid, h):
    i = l
    j = mid + 1
    temp = []
    while i <= mid and j <= h:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j+=1
    
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= h:
        temp.append(arr[j])
        j += 1
    for k in range(len(temp)):
        arr[l + k] = temp[k]
        

def iter_merge(arr):
    n = len(arr)
    size = 1
    last_size = 0
    
    while size <= n/2:
        last_size = size
        
        l = 0
        h = size * 2 - 1
        
        while h <= n-1:
            merge(arr, l, int((l+h)/2), h)
            l = h + 1
            h = l + size * 2 -1
        size *= 2

    if last_size * 2 < n:
        merge(arr, 0, last_size * 2-1, n-1)
        

arr = [8,3,7,2,6,5,9,4]

iter_merge(arr)

print(arr)