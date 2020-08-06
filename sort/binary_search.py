# O(log n)
def binary_search(numbers):
    Find = 55

    print("Numbers list:", numbers)
    print("Find number:", Find)

    low = 0
    mid = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) # 2
        if numbers[mid] > Find:
            high = mid - 1
        elif numbers[mid] < Find:
            low = mid + 1
        else:
            break
    print("Number of searches:", mid)


data_list = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
binary_search(data_list)
