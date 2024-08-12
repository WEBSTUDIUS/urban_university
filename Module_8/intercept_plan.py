def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for num in numbers:
        try:
            result += num
        except TypeError:
            print(f'Unexpected type. Got {type(num)} instead "int" element')
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    try:
        summ = personal_sum(numbers)
        return summ[0] / (len(numbers) - summ[1])
    except ZeroDivisionError as exc:
        return f'Error {exc}'
    except TypeError:
        print(f'Unexpected input. Got {type(numbers)} instead collection containing "int" elements')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
