def count(arr):
    m = max(arr)
    
    empty_arr = [0] * (m+1)
    
    for i in range(len(arr)):
        empty_arr[arr[i]] += 1
    
    i = j = 0
    
    while i < m+1:
        if empty_arr[i] > 0:
            arr[j] = i
            j += 1
            empty_arr[i] -= 1
        else:
            i += 1
            

arr = [6,3,9,10,15,8,6,12,3,6]

count(arr)

print(arr)