def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide_integer(a, b):
    return a // b


def divide(a, b):
    return a / b


def modulo(a, b):
    return a % b


def square(a):
    return a * a


if __name__ == "__main__":
    print("3 + 5 =", add(3, 5))
    print("10 - 4 =", subtract(10, 4))
    print("2 * 3 =", multiply(2, 3))
    print("10 // 4 =", divide_integer(10, 4))
    print("10 / 4 =", divide(10, 4))
    print("10 % 3 =", modulo(10, 3))
    print("3^2 =", square(3))
