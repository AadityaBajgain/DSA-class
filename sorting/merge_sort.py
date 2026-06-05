from merge_two_sorted_list import merge
from merge_two_sorted_section import merge_same_arr
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
    
#     return merge(left,right)

arr = [8,3,6,2,9,34,1,4,5]

# print(merge_sort(arr))

def merge_sort_same_array(arr,l,h):
    if l < h:
        mid = (l+h) // 2
        merge_sort_same_array(arr,l,mid)
        merge_sort_same_array(arr,mid+1,h)
        merge_same_arr(arr,l,mid,h)

merge_sort_same_array(arr,0,len(arr)-1)
print(arr)


