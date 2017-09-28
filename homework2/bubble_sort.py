def bubble_sort(arr):
    n = 1
    order = True

    while order:
        order = False
        for i in range(len(arr) - n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                order = True
        n += 1

    return arr


print(bubble_sort([8, 1, 3, 5]))

"""
Сортировка Пузырьком:
в цикле сравнивается 2 элемента массива
если 1 эелемент больше 2, 
то меняем местами и так до конца цикла. 
После полного прохода по массиву хотя бы 
одно число (а именно – самое большое) 
будет поставлено на свое место
то есть оно будет стоять самым последним, 
значит нам не нужно проверять последний элемент.
После 2 цикла не проверяем последние 2 эелемента и тд.
Но если во время прохода по массиву никакие 
элементы не поменялись местами, значит массив отсортирован,
и на этом можно закончить.
Сложность алгоритма: 
сортировка требует (n - 1)(n - 1) = O(n ** 2) операций
"""
