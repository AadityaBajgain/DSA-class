
"""
Given an array arr[] of positive integers. Find out the maximum perimeter of the triangle from the array.

Note: Return -1, if it is not possible to construct a triangle.

Examples:

Input: arr[] = [6, 1, 6, 5, 8, 4]
Output: 20
Explanation: Triangle formed by  8,6 & 6 has perimeter 20, which is the max possible.

Input: arr[] = [7, 55, 20, 1, 4, 33, 12]
Output:  -1
Explanation: The triangle is not possible because the condition: the sum of two sides should be greater than third is not fulfilled here.

"""
def max_perimeter(arr):
    n = len(arr)
    
    # sort the array in reverse to find the 3 largest numbers
    arr.sort()
    
    # reverse the array to get the largest elements at first
    arr = arr[::-1]
    
    # check if adding two sides is greater then third side (to confirm the property of triangle)
    for i in range(n-2):
        if arr[i] < arr[i+1] + arr[i+2]:
            return arr[i] + arr[i+1] + arr[i+2]
    return -1


print(max_perimeter([6, 1, 6, 5, 8, 4]))