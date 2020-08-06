# O(n^2)
def insert_sort(data: list):
    print("Insertion Sort Start:")
    print("Numbers list:", data)
    length = len(data)

    for i in range(1, length):
        position = i
        while position > 0 and data[position - 1] > data[position]:
            data[position], data[position - 1] = data[position - 1], data[position]
            position -= 1
        print("step:", i, data)
    print("Insertion sort:", data)


data_list = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
insert_sort(data_list)
