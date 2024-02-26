import functools


def dec(func):
    @functools.wraps(func)
    def dec_inner(*args, **kwargs):
        print(f"got {args}, {kwargs}")
        ret = func(*args, **kwargs)
        print("after")
        return ret
    return dec_inner

def dec2(g, firewall):
    def dec2_decorator(func):
        @functools.wraps(func)
        def dec2_inner(*args, **kwargs):
            print(g)
            ret = func(*args, **kwargs)
            print(firewall)
            return ret
        return dec2_inner
    return dec2_decorator

@dec2('hello', 'goodbye')
def f(x: int)->None:
    """This is the docstring"""
    print(f'Hello {x}')

class C:
    def __init__(self, x):
        self.x = x

    @property
    def func(self):
        print("in property y")
        return self.x + 5

    @classmethod
    def func(cls):
        print(f"in classes {cls}")
    @staticmethod
    def func(y):
        print(f"it is normal {y}")

def main():
    f(1)

if __name__ == '__main__':
    exit(main())