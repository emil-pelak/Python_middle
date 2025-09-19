numbers = [3, 1, 4, 1, 5, 9]

for n in numbers:
    print(n)


class MyList:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            current_element = self.data[self.index]
            self.index += 1
            return current_element
        else:
            raise StopIteration


my_list = MyList([1, 2, 3])
print(my_list.data)

for element in my_list:
    print(element)

my_list_iterator = MyList([1, 2, 3]).__iter__()  # Lub iter(MyList([1, 2, 3]))
print(my_list_iterator.__next__())  # Lub next(my_list_iterator)
print(my_list_iterator.__next__())
print(my_list_iterator.__next__())


def number_generator():
    yield 1
    yield 2
    yield 3


generator = number_generator()
print(generator, type(generator))

print(generator.__next__())  # Lub next(generator)
print(generator.__next__())
print(generator.__next__())


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = fibonacci()

for _ in range(500):
    print(next(fib_gen))
