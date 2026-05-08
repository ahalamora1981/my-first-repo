import sys

sys.path.append(".")
from calculator import (
    add,
    subtract,
    multiply,
    square,
    cube,
    divide_integer,
    divide,
    modulo,
)


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 3) == 7


def test_multiply():
    assert multiply(3, 4) == 12


def test_square():
    assert square(4) == 16


def test_cube():
    assert cube(3) == 27


def test_divide_integer():
    assert divide_integer(10, 3) == 3
    assert divide_integer(10, 0) is None


def test_divide():
    assert divide(10, 4) == 2.5


def test_modulo():
    assert modulo(10, 3) == 1


if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_square()
    test_cube()
    test_divide_integer()
    test_divide()
    test_modulo()
    print("All tests passed!")
