"""
    Sum of minimum absolute differences in an array

    Given an array of n distinct integers. The task is to find the sum of minimum absolute difference of each array element. For an element arr[i] present at index i in the array, its minimum absolute difference is calculated as: 

    Min absolute difference (arr[i]) = min(abs(arr[i] - arr[j])), where 0 <= j < n and j != i and abs is the absolute value. 
    Examples: 

    Input : arr = [4, 1, 5]
    Output : 5
    Explanation: Sum of minimum absolute differences is |4-5| + |1-4| + |5-4| = 1 + 3 + 1 = 5

    Input : arr = [5, 10, 1, 4, 8, 7]
    Output : 9
    Explanation: Sum of minimum absolute differences is 
    |5-4| + |10-8| + |1-4| + |4-5| + |8-7| + |7-8| = 1 + 2 + 3 + 1 + 1 + 1 = 9

    Input : arr = [12, 10, 15, 22, 21, 20, 1, 8, 9]
    Output : 18
    
"""


def min_absolute_diff(arr):
    n = len(arr)
    
    # sort the array
    arr.sort()
    
    sum = 0
    
    # this the min abs diff of first num relative to other num in arr(because its sorted)
    sum += arr[1] - arr[0]
    
    # this is the min abs diff of last num
    sum += arr[n-1] - arr[n-2]
    
    # for the remaining middle nums in arr, min diff can be with left or the right nums (we will iterate through the middle numbers and take min diff among left and right)
    for i in range(1,n-1):
        left_diff = arr[i] - arr[i-1]
        right_diff = arr[i+1] - arr[i]
        
        
        sum += min(left_diff, right_diff)
        
    
    return sum

arr = [4, 1, 5]

print(min_absolute_diff(arr))