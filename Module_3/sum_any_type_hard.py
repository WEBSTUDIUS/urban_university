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
        if isinstance(i, str):
            summa += len(i)
        if isinstance(i, list):
            for j in i:
                print(j)
        if isinstance(i, tuple):
            for j in i:
                print(j)
        if isinstance(i, dict):
            for j in i:
                print(j)
    print('SUMMA IS:', summa)


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# converted_list = map(str, data_structure)
# result = ''.join(converted_list)
# print(result)

print(data_structure[-1])
calculate_structure_sum(data_structure)
