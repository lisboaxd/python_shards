from functools import wraps


def coroutine(func):
    '''Decorator: prepare 'func'  guiding it to first yield'''
    @wraps(func)
    def primer(*args, **kw):
        gen = func(*args, **kw)
        next(gen)
        return gen
    return primer
