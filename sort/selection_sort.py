# O(n^2)
def selection_sort(data: list):
    print("Selection Sort Start:")
    print("Numbers list:", data)
    length = len(data)

    for i in range(length - 1):
        min_index = i
        for j in range(i+1, length):
            if data[min_index] > data[j]:
                min_index = j
        data[min_index], data[i] = data[i], data[min_index]
        print("step:", i, data)
    print("Selection sort:", data)


data_list = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
selection_sort(data_list)