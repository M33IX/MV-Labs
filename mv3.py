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

def RectanglesIntegration(a: int, b: int, n: float, h: float, h2: bool) -> float:
    """
    Функция интегрирования методом треугольников
    @param a: int;
    @param b: int;
    @param n: float;
    @param h: float;
    @param h2: bool;
    """
    return 0.0

def TrapezoidIntegration(a: int, b: int, n: float, h: float, h2: bool) -> float:
    """
    Функция интегрирования методом треугольников
    @param a: int;
    @param b: int;
    @param n: float;
    @param h: float;
    @param h2: bool;
    """
    return 0.0

def SimpsonIntegrtion(a: int, b: int, n: float, h: float, h2: bool) -> float:
    """
    Функция интегрирования методом треугольников
    @param a: int;
    @param b: int;
    @param n: float;
    @param h: float;
    @param h2: bool;
    """
    return 0.0