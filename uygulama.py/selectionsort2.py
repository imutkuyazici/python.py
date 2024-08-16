def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min_index = j
        arr[i], arr[min] = arr[min], arr[i]
        print(arr)

numbers = input("Sıralanacak sayıları girin (virgülle ayırarak): ").split(',')
numbers = [int(num) for num in numbers]

selection_sort(numbers)

print("Sıralanmış sayılar:", numbers)
