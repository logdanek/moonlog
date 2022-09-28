#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math  # импорт бибилиотеки
import numpy  # импорт ещё одной бибилиотеки
import matplotlib.pyplot as mpp  # импорт очередной бибилиотеки

# Эта программа рисует график функции, заданной выражением ниже

if __name__ == '__main__':  # проверка, что мы находимся именно в программе
    arguments = numpy.arange(0, 200, 0.1)  # создание списка значений x
    mpp.plot(  # вызов функции (генерирование значений y)
        arguments,
        [math.cos(a) * math.sin(a/50.0) for a in arguments]
    )
    mpp.show()  # вывод графика
