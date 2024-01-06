"""
Author: Batool Alkaddah 
Time & Date: 12:34 p.m. 2024-01-06
PyCharm
"""

def merge_sort(array):
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    merge_sort(left_part)
    merge_sort(right_part)

    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1

        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1