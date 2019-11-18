from math import  pi, sqrt, pow, hypot

def test_filter():
    assert list(filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 9])) == [3, 6, 9]

def test_map():
    assert list(map(lambda x: x, [1, 2, 3])) == [1, 2, 3]
    assert list(map(lambda x: x * 2 + 10, [1, 2, 3])) == [12, 14, 16]
    assert list(map(sqrt, [4, 16, 25])) == [2, 4, 5]

def test_sorted():
    assert sorted([22, 11, 33, 55]) == [11, 22, 33, 55]
    assert sorted([22, 11, 33, 55], key = lambda x: -x) == [55, 33, 22, 11]

def test_pi():
    assert pi == 3.141592653589793

def test_sqrt():
    assert sqrt(16) == 4
    assert sqrt(0) == 0

def test_pow(): #возведение в степень
    assert pow(3, 2) == 9
    assert pow(11, 1) == 11
    assert pow(10, -2) == 0.01

def test_hypot():  #корень квадратный из суммы квадратов
    assert hypot(2, 4) == 4.472135955
    assert hypot(0, 0) == 0
    assert hypot(0, 3) == 3
    assert hypot(-2, -4) == 4.472135955
