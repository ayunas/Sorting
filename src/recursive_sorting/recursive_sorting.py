# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    # # TO-DO
    pass
    
    # return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
#
'''
1. break down array into subarrays
2. recursively call the same function on the subarrays
3. set a base breakout case, when the len(arr) == 1, return the array
4. merge every broken down array, which will start with smallest singular arrays first
5. set indices for all three arrays (left,right,main)
6. while the indexes havent reached the end of BOTH the left and right arrays, compare to see which value is smaller. if left is smaller, set the main array to be the left value
increment the left index and the main index.  if the right is smaller, set the main array to the right value and increment the right index and the main index.
7. once the length of one of the subarrays finishes, set the rest of the remaining subarrays elements to the main array.  have a separate while loop for the left array and one for the right array.  set the main[m] to the left[l] then increment l and m.  and same for the right array, till the end of both subarrays has been met.  then return the altered main array.
'''
import math

def merge_sort(nums):

    if len(nums) == 1:
        return nums


    print('arr in merge_sort', nums)
    mid = math.floor(len(nums) / 2)
    print('mid',mid)
    left = nums[:mid]
    right = nums[mid:]
    print('left',left,'right',right, len(right))
    merge_sort(left)
    merge_sort(right)

    merge(left,right,nums)


   

    return nums

def merge(left,right,main):
    print('in the merge func')
    l = 0 
    r = 0 
    m = 0 #indices for the three arrays

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            main[m] = left[l]
            m = m + 1
            l = l + 1
        else:
            main[m] = right[r]
            m = m + 1
            r = r + 1
    
    while l < len(left):
        main[m] = left[l]
        m = m + 1
        l = l + 1
    
    while r < len(right):
        main[m] = right[r]
        m = m + 1
        r = r + 1
    
    return main

print(merge_sort([5,4,3,2,1,23,4,5]))

# STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r): 
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr
