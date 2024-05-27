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
    Функция интегрирования методом прямоугольников
    @param a: int - нижний предел
    @param b: int - верхний предел
    @param n: float - число узлов разбиения
    @param h: float - шаг разбиения
    @param makeTable: bool - Создание таблицы для вывода на экран
    """
    result = 0
    xi = [a]
    c = list()
    fc = list()

    for i in range(1, int(n)+1):
        xi.append(xi[i-1] + h)
        c.append((xi[i] + xi[i-1]) / 2)
        fc.append(f(c[i-1]))
        result += fc[i-1]

    if makeTable: #Флаг для создания таблицы вычислений
        tables = list()
        xi.pop(0)
        tables.append(xi)
        tables.append(c)
        tables.append(fc)
        MakeTable(tables)
    return result * GetStep(a,b,n)

def TrapezoidIntegration(a: int, b: int, n: float, h: float, makeTable: bool = False) -> float:
    """
    Функция интегрирования методом трапеций
    @param a: int - нижний предел
    @param b: int - верхний предел
    @param n: float - число узлов разбиения
    @param h: float - шаг разбиения
    @param makeTable: bool - Создание таблицы для вывода на экран
    """
    result = 0
    xi = [a]
    yi = list()
    y0 = f(a)

    for i in range (1, int(n) + 1):
        xi.append(xi[i-1] + h)
        yi.append(f(xi[i]))
        result += yi[i - 1]
    result -= yi[len(yi) - 1]

    result += ((y0 + yi[len(yi) - 1]) / 2)

    if makeTable: #Флаг для создания таблицы вычислений
        tables = list()
        xi.pop(0)
        tables.append(xi)
        tables.append(yi)
        MakeTable(tables)

    return result * GetStep(a,b,n)

def SimpsonIntegrtion(a: int, b: int, n: float, h: float, makeTable: bool = False) -> float:
    """
   Функция интегрирования методом симпсона
    @param a: int - нижний предел
    @param b: int - верхний предел
    @param n: float - число узлов разбиения
    @param h: float - шаг разбиения
    @param makeTable: bool - Создание таблицы для вывода на экран
    """
    xi = [a]
    yi = list()
    y0 = f(a)
    oddSum = 0
    evenSum = 0

    #Вычисление до 2n-1
    for i in range (1, int(n)):
        xi.append(xi[i-1] + h)
        yi.append(f(xi[i]))
        if i % 2 != 0:
            oddSum+=yi[i-1]
        else:
            evenSum += yi[i-1]
    #Вычисление 2n
    xi.append(xi[len(xi) - 1] + h)
    yi.append(f(xi[len(xi) - 1]))
    
    result = y0 + (4* oddSum) + (2 * evenSum) + yi[len(yi) - 1]

    if makeTable: #Флаг для создания таблицы вычислений
        tables = list()
        xi.pop(0)
        tables.append(xi)
        tables.append(yi)
        MakeTable(tables)

    return result * (GetStep(a,b,n) / 3)


def MakeTable(listOfTables: list) -> None:
    """Создает таблицу промежуточных вычислений и
    печатает её. Предполагается, что количество элементов в листах
    равное
    @param listOfTables: list - Лист из листов с промежуточными
    вычислениями.
    """
    if listOfTables == []:
        return None
    
    for i in range(len(listOfTables[0])):
        buf = f"{i+1}\t"
        for j in range(len(listOfTables)):
            buf +=f"{listOfTables[j][i]} "
        print(buf)
    return None

a = 0
b = 1
n = GetInitialNodes(a,b, True)
h = GetStep(a,b,n)
SimpsonIntegrtion(a,b,n,h,True)