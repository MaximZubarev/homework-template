def insertion_sort(arr):
    for i in range(1, len(arr)):
        while i > 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1

    return arr


print(insertion_sort([1, 5, 8, 2, 34]))

"""
Сортировка вставками:
сначала берем 2 эелемент в массиве
и сравниваем его с 1
если 2 элемент больше 1, меняем местами.
Далее берем 3 элемент, сравниваем его с 2,
если 3 меньше 2, меняем местами,
после этого 2 элемент сравниваем с 1 итд.
Сложность алгоритма O(n ** 2)
зависит от того, насколько хорошо отсортирован массив.
В лучшем случае время работы — линейно,
в худшем случае — квадратично
"""
