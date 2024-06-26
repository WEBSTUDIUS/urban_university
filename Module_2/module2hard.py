# unreal hard O_o

def result(n):
    secret_keys_first = {}
    secret_keys_second = {}
    for i in range(3, n + 1):
        for j in range(1, i):
            for k in range(1, j):
                if n % (k + j) == 0 and (k + j) != n:
                    if secret_keys_first.get(n):
                        secret_keys_first[n] = [str(k) + str(j), *secret_keys_first[n]]
                    else:
                        secret_keys_first[n] = [str(k) + str(j)]
                elif k + j == n:
                    if secret_keys_second.get(n):
                        secret_keys_second[n] = [str(k) + str(j), *secret_keys_second[n]]
                    else:
                        secret_keys_second[n] = [str(k) + str(j)]

    print(*(sorted(set(*secret_keys_first.values())) + sorted(set(*secret_keys_second.values()))))


num = int(input('Enter number from 3 to 20: '))

while 3 > num < 20 or num > 20:
    num = int(input('Enter number from 3 to 20: '))

result(num)
