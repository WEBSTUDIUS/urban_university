import time


def bubble_sort(ls):
    # начальное время
    start_time = time.time()

    for i in range(len(ls) - 1, 0, -1):
        for j in range(i):
            if ls[i] > ls[j + 1]:
                ls[i], ls[j + 1] = ls[j + 1], ls[i]
    # конечное время
    end_time = time.time()
    # разница между конечным и начальным временем
    elapsed_time = end_time - start_time
    print(f'Elapsed time {bubble_sort.__name__}: ', elapsed_time)

    return ls


def selection_sort(ls):
    # начальное время
    start_time = time.time()

    for i in range(len(ls) - 1):
        min_index = i
        for j in range(i + 1, len(ls)):
            if ls[min_index] > ls[j]:
                min_index = j
                ls[min_index], ls[j] = ls[j], ls[min_index]
    # конечное время
    end_time = time.time()
    # разница между конечным и начальным временем
    elapsed_time = end_time - start_time
    print(f'Elapsed time {selection_sort.__name__}: ', elapsed_time)

    return ls


def insertion_sort(ls):
    # начальное время
    start_time = time.time()
    for i in range(1, len(ls)):
        key = ls[i]
        j = i - 1
        while ls[i] > key and j >= 0:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = key

    # конечное время
    end_time = time.time()
    # разница между конечным и начальным временем
    elapsed_time = end_time - start_time
    print(f'Elapsed time {insertion_sort.__name__}: ', elapsed_time)

    return ls
