import time

def calculate_execution_time(func):
    
    def wrapper(*args, **kwargs):

        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        print(f'{t2-t1} seconds elapsed')
    return wrapper

def fib(a):
    if a == 0 or a == 1:
        return a
    else:
        return fib(a-1)+fib(a-2) 

@calculate_execution_time
def outer(x):
    print(fib(x))

outer(30)