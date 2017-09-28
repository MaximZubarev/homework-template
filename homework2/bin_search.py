def bin_search(arr, key):
    left = -1
    right = len(arr)
    while right > left + 1:
        middle = (left + right) // 2
        if arr[middle] > key:
            right = middle
        else:
            left = middle

    if arr[left] >= 0 and arr[left] == key:
        return "number is " + str(left + 1)
    else:
        return "nothing"


print(bin_search([2, 6, 10, 56, 100, 0, 21], 11))


"""
Бинарный поиск:
находим средний элемент, сравниваем его с искомым, 
если искомый меньше, то ищем в левой части массива, иначе в правой итд.
Тем самым, длина части, в которой мы ищем элемент, 
сокращается в два раза на каждом шаге цикла, 
значит, общая сложность алгоритма двоичного поиска будет O(log n)
"""
