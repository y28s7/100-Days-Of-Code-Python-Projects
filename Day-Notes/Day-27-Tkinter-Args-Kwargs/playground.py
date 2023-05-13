def add(*args):
    result = 0
    for n in args:
        result += n
    return result


print(add(8678, 7, 6787, 8, 554, 43, 653, 4567, 687, 68, 545, 353465, 6767, 78, 64, 4, 5, 7, 6, 887, 8 * 9 ** 8))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(model="Model X")  # if does not specify anything, will return none
print(my_car.make, ":", my_car.model)
