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
            j += 1
    
    while i<= mid:
        temp.append(arr[i])
        i += 1
    while j<= h:
        temp.append(arr[j])
        j+=1
    
    for k in range(len(temp)):
        arr[l+k] = temp[k]
    

def recursive_merge(arr, l, h):
    if l < h:
        mid = (l+h)//2
        
        recursive_merge(arr, l, mid)
        recursive_merge(arr, mid+1, h)
        
        merge(arr,l,mid, h)
        

arr = [8,3,7,2,6,5,9,4]
n = len(arr)
recursive_merge(arr,0,n-1)

print(arr)