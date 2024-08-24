class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('Step cant be a zero value')
        self.start, self.stop, self.step, self.pointer, self.i = start, stop, step, start, 0

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        self.pointer += self.step
        self.i += 1
        if (self.step < 0 and self.pointer < self.stop) or (self.step > 0 and self.pointer > self.stop):
            raise StopIteration('Done')

        if self.i == 1:
            self.pointer -= self.step
            return self.start

        return self.pointer


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError as e:
    print(e)

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
