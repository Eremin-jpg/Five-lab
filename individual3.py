#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def divizible(number):
    """
    Проверяет, делится ли число на сумму своих цифр.
    """
    digits_sum = sum(int(digit) for digit in str(number))
    return number % digits_sum == 0

def two_digit():
    """
    Определяет все двузначные числа, которые делятся на сумму своих цифр.
    """
    results = []
    for number in range(10, 100):
        if divizible(number):
            results.append(number)
    return results

if __name__ == '__main__':
    divisible_numbers = two_digit()
    print("Двузначные числа, которые делятся на сумму своих цифр:")
    print(", ".join(map(str, divisible_numbers)))
