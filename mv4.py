import math
import pandas as pd
from tabulate import tabulate

def f(x: float, y: float) -> float:
    """Возвращает правую часть дифференциального уравнения"""
    return 0.0

def AnalyticSolution(x: float) -> float:
    """Возращает точное аналитическое решение дифференциального 
    уравнения"""
    return 0.0

def TureValue(x: list[float], n: int)-> list[float]:
    """Возвращает точное значение в заданых точках x"""
    return list(0)

def CalculateEuler(x: list[float], y: list[float], n: int, h: float) -> list[float]:
    """Возвращает решение численного дифференциального 
    уравнения по методу Эйлера"""
    return list(0)

def CalculateEulerModified(x: list[float], y: list[float], n: int, h: float) -> list[float]:
    """Производит вычисление по модифицированному
    методу Эйлера"""
    return list(0)

def CalculateRungeKutta(x: list[float], y: list[float], n: int, h: float) -> list[float]:
    """Производит вычисление по методы Рунге-Кутты"""
    return list(0)

def MakeTable() -> None:
    """Мне уже"""
    pass

def CalculateError() -> None:
    """Просто похуй"""
    pass