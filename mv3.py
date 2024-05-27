import numpy as np
import math

def TrueValue() -> float:
    """Заранее известное истинное значение интеграла"""
    return ( math.e * (math.e - 1) ) + math.log(2)

def Precision() -> float:
    """Точность для оценки погрешности"""
    return 0.0001

def f(x: float) -> float:
    """Возвращает функцию для интегрирования"""
    return math.exp(x) + (1 / x)

def GetInitialNodes(a: int, b :int, simpson :bool = False) -> float:
    """
    Возвращает начальное число узлов
    для методов Симпсона и трапеций и треугольников
    @param a: Нижний предел интегрирования
    @param b: Верхний предел интегрирования
    @param simpson: Выбор метода. По умолчанию для трапеций и прямоугольников
    """
    return ( int((b - a) / (2 * pow(Precision(), 0.25))) + 1 ) if simpson else (((b - a) / np.sqrt(Precision())) // 1 + 1 )

def GetStep(a: int, b: int, n: float) -> float:
    """Находит шаг для методов Симпсона и методов прямогульников и трапеций
    @param a: Нижний предел интегрирования
    @param b: Верхний предел интегрирования
    @param n: Число узлов для разбиения
    """
    return (b - a) / n

def RectanglesIntegration(a: int, b: int, n: float, h: float, makeTable: bool = False) -> float:
    """
    Функция интегрирования методом треугольников
    @param a: int - нижний предел
    @param b: int - верхний предел
    @param n: float - число узлов разбиения
    @param h: float - шаг разбиения
    @param makeTable: bool - Создание таблицы для вывода на экран
    """
    result = 0
    x = list()
    c = list()
    fc = list()
    x.append(a)
    for i in range(1, n+1):
        x.append(x[i-1] + h)
        c.append((x[i] + x[i-1]) / 2)
        fc.append(f(c[i-1]))
        result += f(c[i-1])
    if makeTable: #Флаг для создания таблицы вычислений
        tables = list()
        tables.append(x)
        tables.append(c)
        tables.append(fc)
        MakeTable(tables)
    return result * ((b-a)/n)

def TrapezoidIntegration(a: int, b: int, n: float, h: float, makeTable: bool) -> float:
    """
    Функция интегрирования методом треугольников
    @param a: int - нижний предел
    @param b: int - верхний предел
    @param n: float - число узлов разбиения
    @param h: float - шаг разбиения
    @param makeTable: bool - Создание таблицы для вывода на экран
    """
    result = 0
    xi = list()
    yi = list()
    x = a
    y0 = f(x)

    for i in range (0, n - 1):
        x += h
        xi.append(x)
        result += f(x)
        yi.append(result)
    x+=h
    xi.append(x)
    yi.append(f(x))
    result += ((y0 + f(x)) / 2)
    
    if makeTable: #Флаг для создания таблицы вычислений
        tables = list()
        tables.append(xi)
        tables.append(yi)
        MakeTable(tables)

    return ((b-a) / n) * result

def SimpsonIntegrtion(a: int, b: int, n: float, h: float, makeTable: bool) -> float:
    """
   Функция интегрирования методом треугольников
    @param a: int - нижний предел
    @param b: int - верхний предел
    @param n: float - число узлов разбиения
    @param h: float - шаг разбиения
    @param makeTable: bool - Создание таблицы для вывода на экран
    """
    return 0.0

def MakeTable(listOfTables: list) -> None:
    return None
