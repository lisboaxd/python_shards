
from inspect import getgeneratorstate


def simple_coroutine():
    print("> coroutine started")
    value = yield
    print(f"> coroutine received: {value}")


my_coroutine = simple_coroutine()

next(
    my_coroutine
)  # my_coroutine.send(None) also works. This will initialize, process called "priming"


def simple_coro2(a):
    print(f'-> Started: a = {a}')
    b = yield a
    print(f'-> received: b = {b}')
    c = yield a + b
    print(f'-> received: c = {c}')


my_coro2 = simple_coro2(14)
next(my_coro2)  # -> Started: a = 14
my_coro2.send(28)  # -> Received: b = 28
my_coro2.send(99)  # -> Received: c = 99
