#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math #импорт бибилиотеки 
import numpy #импорт бибилиотеки
import matplotlib.pyplot as mpp #импорт бибилиотеки

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__': #что-то похожее на C++
    arguments = numpy.arange(0, 200, 0.1) #по всей видимости создание списка
    mpp.plot( #вызов функции
        arguments,
        [math.cos(a) * math.sin(a/50.0) for a in arguments]
    )
    mpp.show() #вывод полученных вкусняшек на экран
