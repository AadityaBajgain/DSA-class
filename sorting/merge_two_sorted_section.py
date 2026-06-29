def merge_same_arr(arr,l,m,h):
    
    temp = []
    
    i = l
    j = m + 1
    
    while i <= m and j <= h:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j+=1
    
    while i <= m:
        temp.append(arr[i])
        i+=1
    while j <= h:
        temp.append(arr[j])
        j+=1
        
    for k in range(len(temp)):
        arr[l + k] = temp[k]