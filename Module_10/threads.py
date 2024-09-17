from time import sleep, time
from threading import Thread
from time import sleep


def write_words(word_count, file_name):
    with open(file_name, 'a') as file:
        for i in range(word_count):
            file.write('Some word N' + str(i + 1) + '\n')
            sleep(0.1)
    print(f'Writing into file {file_name} was finished')


start_time = time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = time()
print(f'Time step-by-step is {end_time - start_time} sec.')

start_time = time()
t1 = Thread(target=write_words, args=(10, 'example1.txt'))
t2 = Thread(target=write_words, args=(30, 'example2.txt'))
t3 = Thread(target=write_words, args=(200, 'example3.txt'))
t4 = Thread(target=write_words, args=(100, 'example4.txt'))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
end_time = time()
print(f'Time threads is {end_time - start_time} sec.')
