class StepValueError(ValueError):
    pass

class Iterator:

    def __init__(self,start,stop,step = 1):
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        self.start , self.stop, self.step = start, stop, step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start-self.step
        return self

    def __next__(self):
        self.pointer += self.step
        if self.step < 0 and self.pointer < self.stop or self.step > 0 and self.pointer > self.stop:
            raise StopIteration
        return self.pointer

def go_iter(start,stop,step=1):
    try:
        iter_ = Iterator(start, stop,step)
        for i in iter_:
            print(i, end=' ')
        print()
    except StepValueError:
        print('Шаг указан неверно')

go_iter(100,200,0)
go_iter(-5, 1)
go_iter(6, 15, 2)
go_iter(5, 1, -1)
go_iter(10, 1)

