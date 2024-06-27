# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Используя этот список составьте второй список primes содержащий только простые числа.
# А так же третий список not_primes, содержащий все не простые числа.
# Выведите списки primes и not_primes на экран(в консоль).
# Пункты задачи:
#
# Создайте пустые списки primes и not_primes.
# При помощи цикла for переберите список numbers.
# Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
# Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
# В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes в зависимости от значения переменной is_prime после проверки (True - в prime, False - в not_prime).
# Выведите списки primes и not_primes на экран(в консоль).

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numbers = [3, 6, 3, 2, 7, 12, 11, 56, 33, 55, 9, 8, 13, 14, 15]

primes = []
not_primes = []

for i in numbers:
    if i == 1:
        continue
    is_prime = True
    for j in numbers:
        if j > i:
            break
        if i % j == 0 and j > 1 and j != i:
            is_prime = False
    if not is_prime:
        not_primes.append(i)
    else:
        primes.append(i)

print(primes, not_primes)

