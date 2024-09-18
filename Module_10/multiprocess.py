import multiprocessing
import time


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            all_data.append(line.strip())


filenames = [f'./files/file {number}.txt' for number in range(1, 5)]

# Line call
# start = time.time()
# for filename in filenames:
#     read_info(filename)
# finish = time.time()
# print(f'Time to line seq reading all files: {round(finish - start, 4)} seconds')

# Multiprocessing
if __name__ == '__main__':
    start = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    finish = time.time()
    print(f'Time to miltiprocess seq reading all files: {round(finish - start, 4)} seconds')
