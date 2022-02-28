class DemoException(Exception):
    '''A kind of exception to demonstrate'''


def demonstrate_exc_finally():
    print('-> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoExcepetion handled. Continuining...')
            else:
                print('-> Coroutine receied: {!r}'.format(x))
    finally:
        print('-> coroutine ending')


coro_finally = demonstrate_exc_finally()
next(coro_finally)
coro_finally.send(20)
coro_finally.send(50)
