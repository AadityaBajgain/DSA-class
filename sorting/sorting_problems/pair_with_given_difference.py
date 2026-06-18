"""
Given an unsorted array and an integer x, the task is to find if there exists a pair of elements in the array whose absolute difference is x. 

Examples: 

Input: arr[] = [5, 20, 3, 2, 50, 80], x = 78
Output: true
Explanation: The pair is {2, 80}.

Input: arr[] = [90, 70, 20, 80, 50], x = 45
Output: false
Explanation: No such pair exists.

"""

def pair_diff(arr, dif):
    
    n = len(arr)
    
    arr.sort()
    
    j = 1
    # use 2 pointers to compare the difference  
    for i in range(n):
        if j <= i:
            j+=1
        # move j forward until the difference is smaller than given target
        while j < n and arr[j] - arr[i] < dif:
            j += 1
        # 
        if j<n and arr[j] - arr[i] == dif:
            return True
    return False


arr = [90, 70, 20, 80, 50]
arr2 = [5, 20, 3, 2, 50, 80]

print(pair_diff(arr,45))
print(pair_diff(arr2,78))