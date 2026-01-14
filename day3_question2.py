import time
from functools import wraps


def execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"'{func.__name__}' executed in {elapsed_time:.4f} seconds")
        return result
    return wrapper
@execution_time
def addition(a,b):
    time.sleep(0.2)
    return a+b

print(addition(10,15))