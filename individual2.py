#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


def biquadratic(a, b, c):
    """
    Решает биквадратное уравнение вида: a*x^4 + b*x^2 + c = 0.
    Возвращает сообщение о количестве действительных корней и сами корни.
    """
    if a == 0:
        raise ValueError("Коэффициент 'a' не может быть равен 0.")

    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return "Нет действительных корней."

    roots = []

    if discriminant == 0:
        z = -b / (2 * a)
        if z >= 0:
            roots.extend([math.sqrt(z), -math.sqrt(z)])
        return roots if roots else "Нет действительных корней."

    # Если дискриминант > 0
    z1 = (-b + math.sqrt(discriminant)) / (2 * a)
    z2 = (-b - math.sqrt(discriminant)) / (2 * a)

    if z1 >= 0:
        roots.extend([math.sqrt(z1), -math.sqrt(z1)])
    if z2 >= 0:
        roots.extend([math.sqrt(z2), -math.sqrt(z2)])

    return roots if roots else "Нет действительных корней."


if __name__ == '__main__':
    try:
        # Ввод коэффициентов
        a = float(input("Введите коэффициент a: "))
        b = float(input("Введите коэффициент b: "))
        c = float(input("Введите коэффициент c: "))

        # Решение уравнения
        result = biquadratic(a, b, c)

        # Вывод результата
        if isinstance(result, str):
            print(result)
        else:
            print(f"Действительные корни: {', '.join(map(str, result))}")
    except ValueError as e:
        print(f"Ошибка: {e}")
