# O(nlogn)
def merge_sort(array):
    if len(array) > 1:
        mid = len(array)  # 2

        # left_array, get item before mid from array
        left_array = array[:mid]

        # right_array, get item after mid from array
        right_array = array[mid:]

        merge_sort(left_array)
        merge_sort(right_array)

        right_index = 0
        left_index = 0
        merged_index = 0

        while right_index < len(right_array) and left_index < len(left_array):
            if (right_array[right_index] < left_array[left_index]):
                array[merged_index] = right_array[right_index]
                right_index = right_index + 1
            else:
                array[merged_index] = left_array[left_index]
                left_index = left_index + 1

        while right_index < len(right_array):
            array[merged_index] = right_array[right_index]
            right_index = right_index + 1
            merged_index = merged_index + 1

        while left_index < len(left_array):
            array[merged_index] = left_array[left_index]
            left_index = left_index + 1
            merged_index = merged_index + 1