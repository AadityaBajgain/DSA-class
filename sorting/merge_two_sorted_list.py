def merge(arr1,arr2):
    m = len(arr1)
    n = len(arr2)
    arr3 = [None] * (m+n)
    i = j = k = 0
    
    while i < m and j < n:
        if arr1[i] <= arr2[j]:
            arr3[k] = arr1[i]
            k += 1
            i += 1
        else:
            arr3[k] = arr2[j]
            k += 1
            j += 1
    
    for l in range(i,m):
        arr3[k] = arr1[l]
        k += 1
    for r in range(j, n):
        arr3[k] = arr2[r]
        k += 1
    
    return arr3


if __name__ == "__main__":
    a = [2,18,10,20,23]
    b = [4,9,19,25]

    print(merge(a,b))