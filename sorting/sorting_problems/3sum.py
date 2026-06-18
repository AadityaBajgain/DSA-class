"""
Given an array arr[] and an integer sum, check if there is a triplet in the array which sums up to the given target sum.

Examples: 

Input: arr[] = [1, 4, 45, 6, 10, 8], target = 13
Output: true
Explanation: The triplet [1, 4, 8] sums up to 13

Input: arr[] = [1, 2, 4, 3, 6, 7], target = 10 
Output: true
Explanation: The triplets [1, 3, 6] and [1, 2, 7] both sum to 10. 

Input: arr[] = [40, 20, 10, 3, 6, 7], sum = 24 
Output: false
Explanation:  No triplet in the array sums to 24.
"""

# 1 4 6 8 10 45
def three_sum(arr, target):
    
    arr.sort()
    
    n = len(arr)
    for i in range(n-2):
        
        l = i+1
        r = n-1
        
        required_sum = target - arr[i]
        while l < r:
            if arr[l] + arr[r] == required_sum:
                return True
            if arr[l] + arr[r] < required_sum:
                l += 1
            else:
                r -= 1
    return False 



arr = [1, 4, 45, 6, 10, 8]
target = 13

print(three_sum(arr, target))
        
arr2 = [40, 20, 10, 3, 6, 7]
target2 = 24

print(three_sum(arr2,target2))