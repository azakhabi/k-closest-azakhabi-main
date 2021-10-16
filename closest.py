def closest(array: list, target: int, count: int) -> list:
    """Находит в упорядоченном массиве `array` `count` чисел, ближайших по значению к `target`.
    :param array: массив, в котором идёт поиск
    :param target: число, от которого отсчитываются ближайшие
    :param count: количество чисел, которые необходимо выдать
    """
    s, e = 0, len(array)
    f = []
    while True:
        if len(array[s:e]) == 1:
            ix = s
            break
        else:
            if target < array[s + (e - s) // 2]:
                e -= (e - s) // 2
            else:
                s += (e - s) // 2
    for i in range(ix - count + 1, ix + count):
        if 0 <= i < len(array):
            f.append(array[i])
    res = []
    for i in f:
        res.append((abs(i - target), i))
    res.sort()
    result = [res[i][1] for i in range(count)]
    return sorted(result)


