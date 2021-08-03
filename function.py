# funciton decoration?

from functools import wraps

def check_first_positive(func):
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        if len(args) > 1 and args[0] > 0:
            pass
        else:
            raise Exception('first argument not positive')

        return func(*args)
    return func_wrapper


@check_first_positive
def testFunc (first, second, *args, **kwargs):
    print ('first', first)
    print ('second', second)

    for arg in args:
        print ('arg ', args.index(arg), arg)

    for kwarg in kwargs:
        print ('arg ', kwarg, kwargs[kwarg])