#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def month_name(month):
    """Возвращает название месяца по номеру."""
    months = [
        "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
        "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
    ]

    if 1 <= month <= 12:
        return months[month - 1]
    else:
        return "Ошибка: Неверный номер месяца"


if __name__ == '__main__':
    month = int(input("Введите номер месяца (от 1 до 12): "))
    print(month_name(month))

