"""
This python script contains the function find_max_val_unimodal_arr() that
searches for the maximum value number in a given list and returns it.
"""

__author__ = "Tolulope Oshinowo"
import pytest
import math

def find_max_val_unimodal_arr(unimodal_arr):
    """
    This function works by taking the index at the center of the list and
    comparing it to the values immediately to its left and right to determine
    which side should be further examined to find the maximum. Once a side is
    chosen (based on the respective adjacent value being greater than the
    center value), the list is updated to cutoff at the previous center and a
    new center, left, and right are assigned for the process to repeat until
    the maximum is found).
    """
    arr = unimodal_arr
    maxfound = False
    if (len(arr) == 0):
        print('empty list')
        return -1

    center = math.floor(len(arr)/2)
    left = (math.floor(len(arr)/2)-1) if (math.floor(len(arr)/2)-1) >= 0 else 0
    right = (math.floor(len(arr)/2)+1) if (math.floor(len(arr)/2)+1) <= (len(arr)-1) else (len(arr)-1)

    if (len(arr) == 1):
        print('maximum value = ' + str(arr[center]))
        return arr[center]

    if (len(arr) == 2):
        print('maximum value = ' + str(arr[left] if arr[left] > arr[right] else arr[right]))
        return arr[left] if arr[left] > arr[right] else arr[right]

    while (not maxfound):
        if (arr[left] > arr[center]):
            arr = arr[:center]
            center = math.floor(len(arr)/2)
            left = (math.floor(len(arr)/2)-1) if (math.floor(len(arr)/2)-1) >= 0 else 0
            right = (math.floor(len(arr)/2)+1) if (math.floor(len(arr)/2)+1) <= (len(arr)-1) else (len(arr)-1)
        if (arr[right] > arr[center]):
            arr = arr[center:]
            center = math.floor(len(arr)/2)
            left = (math.floor(len(arr)/2)-1) if (math.floor(len(arr)/2)-1) >= 0 else 0
            right = (math.floor(len(arr)/2)+1) if (math.floor(len(arr)/2)+1) <= (len(arr)-1) else (len(arr)-1)
        if ((arr[right] <= arr[center]) and (arr[left] <= arr[center])):
            maxfound = True

    print('maximum value = ' + str(arr[center]))
    return arr[center]
