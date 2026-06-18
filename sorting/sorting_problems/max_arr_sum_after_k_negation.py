"""
    Maximize array sum after K negations

    Given an array of size n and an integer k. We must modify array k number of times. In each modification, we can replace any array element arr[i] by -arr[i]. The task is to perform this operation in such a way that after k operations, the sum of the array is maximum.

    Examples : 

    Input : arr[] = [-2, 0, 5, -1, 2], k = 4
    Output: 10
    Explanation:
    1. Replace (-2) by -(-2), array becomes [2, 0, 5, -1, 2]
    2. Replace (-1) by -(-1), array becomes [2, 0, 5, 1, 2]
    3. Replace (0) by -(0), array becomes [2, 0, 5, 1, 2]
    4. Replace (0) by -(0), array becomes [2, 0, 5, 1, 2]

    Input : arr[] = [9, 8, 8, 5], k = 3
    Output: 20
    Explanation: Negate 5 three times. Array will become [9, 8, 8, -5]. 

    """
    

# def max_sum_after_k_negation(arr,k):
    
#     # sort the array to get smaller number at first
#     arr.sort()
    
#     # loop through it k times for negation
#     for i in range(k):
#         # if the element is the min in the list, negate
#         if arr[i] == min(arr):
#             arr[i] = -arr[i]
    
#     return sum(arr)
    
# # arr = [9, 8, 8, 5]
# arr = [-2, 0, 5, -1, 2]
# result = max_sum_after_k_negation(arr,3)

# print(result)


# optimized approach

def max_sum_after_k_negation(arr,k):
    
    i = 0
    n = len(arr)
    
    arr.sort()
    
    # loops through the array until the negative element are negated, and k > 0
    while i < n and k > 0 and arr[i] <= 0:
        arr[i] *= -1
        k -= 1
        i += 1
        
    
    # if done with the negative integers, we need to negate the remaining integers
    # since all remaining elements are positive, we can negate the min element even times so that it remains the same, hence it makes no sense to negate it at all
    
    k = k % 2
    
    #  so if k == 0, return the total sum
    if k == 0:
        return sum(arr)
    
    # if k was odd number, the remainder would be 1, we need to negate the min value
    
    return sum(arr) - 2 * min(arr)


arr = [9, 8, 8, 5]
# arr = [-2, 0, 5, -1, 2]
result = max_sum_after_k_negation(arr,3)

print(result)