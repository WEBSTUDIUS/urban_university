from random import choice

# part 1
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))


# part 2
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, 'w')
        for data in data_set:
            file.write(str(data) + '\n')
        file.close()

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# part 3
class MysticBall:
    def __init__(self, *words_list):
        self.words_list = words_list

    def __call__(self):
        return choice(self.words_list)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
