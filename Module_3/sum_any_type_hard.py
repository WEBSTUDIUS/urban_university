# Что должно быть подсчитано:
#
# Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# Все строки (не важно, являются они ключами или значениям или ещё чем-то)
#
# Для примера, указанного выше, расчёт вёлся следующим образом:
#
# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99
#
# Входные данные (применение функции):
#
# data_structure = [
#   [1, 2, 3],
#   {'a': 4, 'b': 5},
#   (6, {'cube': 7, 'drum': 8}),
#   "Hello",
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]

def calculate_structure_sum(data):
    summa = 0

    for i in data:
        if isinstance(i, int) or isinstance(i, float):
            summa += i
        elif isinstance(i, str):
            summa += len(i)
        elif isinstance(i, list):
            summa += calculate_structure_sum(i)
        elif isinstance(i, tuple):
            summa += calculate_structure_sum(i)
        elif isinstance(i, dict):
            for key, value in i.items():
                if hasattr(key, '__iter__'):
                    summa += calculate_structure_sum(key)
                else:
                    if isinstance(key, int) or isinstance(key, float):
                        summa += key
                    elif isinstance(key, str):
                        summa += len(key)
                if hasattr(value, '__iter__'):
                    summa += calculate_structure_sum(value)
                else:
                    if isinstance(value, int) or isinstance(value, float):
                        summa += value
                    elif isinstance(value, str):
                        summa += len(value)
        elif isinstance(i, set):
            summa += calculate_structure_sum(i)
    return summa


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


print(calculate_structure_sum(data_structure))