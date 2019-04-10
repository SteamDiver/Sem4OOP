import time

def slept(func):
    def wrapper(a, b):
        time.sleep(3)
        return func(a, b)
    return wrapper

@slept
def add(a, b):
    return a + b

print(add(1, 2))
