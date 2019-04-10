import random as rnd

def unstable(func):
    def wrapper():
        if rnd.randint(0, 1) > 0:
            return func()
        else:
            print("Не в этот раз")
    return wrapper

@unstable
def test():
    print("Сдам урмат")

test()
