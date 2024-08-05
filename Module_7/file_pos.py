def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')

    for string in strings:
        strings_positions[(strings.index(string) + 1, file.tell())] = string
        file.write(string + '\n')
    file.close()

    return strings_positions


info = [
    'Text for tell.', # вывод, как в ДЗ, требует дополнительного знака
    'Используйте кодировку utf-8.',  # вывод, как в ДЗ, требует дополнительного знака
    'Because there are 2 languages!',  # вывод, как в ДЗ, требует дополнительного знака
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
