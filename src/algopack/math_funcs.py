"""
Модуль с реализациями факториала и чисел Фибоначчи.

Сигнатуры соответствуют заданию лабораторной работы 3:
- factorial(n: int) -> int
- factorial_recursive(n: int) -> int
- fibo(n: int) -> int
- fibo_recursive(n: int) -> int
"""


def factorial(n: int) -> int:
    """
    Итеративный факториал n (n!).
    Определён только для n >= 0, иначе выбрасывает ValueError.
    """
    if n < 0:
        raise ValueError("factorial is not defined for negative integers")

    result = 1
    for k in range(2, n + 1):
        result *= k
    return result


def factorial_recursive(n: int) -> int:
    """
    Рекурсивный факториал n (n!).
    Определён только для n >= 0, иначе выбрасывает ValueError.
    """
    if n < 0:
        raise ValueError("factorial is not defined for negative integers")

    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def fibo(n: int) -> int:
    """
    Итеративное n-е число Фибоначчи.
    Используется стандартное определение:
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) для n >= 2.
    """
    if n < 0:
        raise ValueError("fibonacci is not defined for negative integers")

    if n == 0:
        return 0
    if n == 1:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


def fibo_recursive(n: int) -> int:
    """
    Рекурсивное n-е число Фибоначчи.
    То же определение, что и в fibo, но через прямую рекурсию.
    Подходит только для небольших n.
    """
    if n < 0:
        raise ValueError("fibonacci is not defined for negative integers")

    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)
