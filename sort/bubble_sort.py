# O(N^2)
def bubble_sort(data: list):
    # 定義資料長度
    length = len(data)
    for i in range(length-2):                   # 有 n 個資料長度，但只要執行 n-1 次
        for j in range(length-i-1):             # 從第1個開始比較直到最後一個還沒到最終位置的數字
            if data[j] > data[j+1]:        # 比大小然後互換
                data[j], data[j+1] = data[j+1], data[j]

        print("step:", i + 1, ":", data)


data_list = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
bubble_sort(data_list)
