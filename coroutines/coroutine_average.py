from coroutine_utils import coroutine
from inspect import getgeneratorstate


@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count


avg_coroutine = averager()
print(getgeneratorstate(avg_coroutine))
print(avg_coroutine.send(10))
print(avg_coroutine.send(30))
print(avg_coroutine.send(5))
