import functools


def dec(beg, end):
    def dec_decorator(func):
        @functools.wraps(func)
        def dec_inner(*args, **kwargs):
            print(beg)
            ret = func(*args, **kwargs)
            print(end)
            return ret
        return dec_inner
    return dec_decorator

@dec("Begin", "End")
def f(x:int):
    """This is description"""
    for i in range(4, x):
        print(f'Number {i}')


def main():
    f(1)

if __name__=="__name__":
    exit(main())