from inspect import getgeneratorstate


class DemoException(Exception):
    '''A kind of exception to demonstrate'''


def demonstrate_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoExcepetion handled. Continuining...')
        else:
            print('-> Coroutine receied: {!r}'.format(x))
    raise RuntimeError('this line should never run')


exc_coroutine = demonstrate_exc_handling()
next(exc_coroutine)
exc_coroutine.send(11)
exc_coroutine.send(22)
exc_coroutine.close()
print(getgeneratorstate(exc_coroutine))

# testing Throw of Excepetion on coroutine
exc_coroutine = demonstrate_exc_handling()
next(exc_coroutine)
exc_coroutine.send(11)
exc_coroutine.throw(DemoException)
exc_coroutine.send(22)
print(getgeneratorstate(exc_coroutine))
