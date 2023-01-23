
def validate(func):
    def wrapper(*args, **kwargs):
        d = func.__annotations__
        print(d)
        params = list(d.keys())
        print(params)
        for p, arg in zip(params, args):
            print(p, arg)
            if not isinstance(arg, d[p]):
                raise TypeError(f'"""{arg}""" - not a valid argument, must be {d[p]}')
        return func(*args, **kwargs)
    return wrapper

@validate
def add(a: int, b: int) -> int:
    return a + b

print(add(1, '2'))

