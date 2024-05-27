import math
import pandas as pd
from tabulate import tabulate

def f(x: float, y: float) -> float:
    """Возвращает правую часть дифференциального уравнения"""
    return 0.0

def AnalyticSolution(x: float) -> float:
    """Возращает точное аналитическое решение дифференциального 
    уравнения
    """
    return 0.0

def TureValue(x: float, n: int)-> list:
    """Возвращает точное значение в заданых точках x"""
    return 1

def CalculateEuler(x: float, y: float, n: int, h: float) -> list:
    """Возвращает решение численного дифференциального 
    уравнения по методу Эйлера
    """
    return 0.0