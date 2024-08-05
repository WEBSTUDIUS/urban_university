def custom_write(file_name, strings):
    res = {}
    file = open(file_name, 'w', encoding='utf-8')

    for string in strings:
        res[(strings.index(string) + 1, file.tell())] = string
        file.write(string + '\n')
    file.close()

    return res


info = [
    'Text for tell.', # вывод, как в ДЗ, требует дополнительного знака
    'Используйте кодировку utf-8.',  # вывод, как в ДЗ, требует дополнительного знака
    'Because there are 2 languages!',  # вывод, как в ДЗ, требует дополнительного знака
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
