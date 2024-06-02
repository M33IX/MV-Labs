import math

def f(x: float, y: float) -> float:
    """Возвращает правую часть дифференциального уравнения"""
    return y + math.pow(x,2)

def AnalyticSolution(x: float) -> float:
    """Возращает точное аналитическое решение дифференциального 
    уравнения"""
    return -(math.pow(x, 2)) - 2*x + 5*math.exp(x) - 2

def TureValue(x: list[float], n: float)-> list[float]:
    """Возвращает точное значение в заданых точках x"""
    y = list()
    for i in range(1, n+1):
        y.append(AnalyticSolution(x[i]))
    return y

def CalculateIterations(method:function, x: list[float], y0: float, n: float, h: float) -> list[float]:
    y = [y0]
    deltayi = list()
    for i in range(0, int(n)):
        result = method(x[i], y[i], h)
        deltayi.append(result[0])
        y.append(result[1])
    deltayi.append(0)
    MakeTable()
    return y

def EulersMethod(x: float, y: float, h: float) -> tuple[float, float]:
    """Считает значение прироста и значение y на одной итерации"""
    deltayi = h * f(x,y)
    y += deltayi
    return (deltayi, y)

def ModifiedEulersMethod(x: float, y: float, h: float) -> tuple[float, float]:
    """Считает значение прироста и значение y на одной итерации"""
    y2 = (h / 2) * f(x,y)
    deltayi = h * f(x + (h / 2), y + y2)
    y += deltayi
    return (deltayi, y)

def RungeKuttasMethod(x: float, y: float, h: float) -> tuple[float, float]:
    """Считает значение прироста и значение y на одной итерации"""
    k1 = h * f(x, y)
    k2 = h * f(x + ( h / 2 ), y + (k1 / 2))
    k3 = h * f(x + h, y + 2 * k2 - k1)
    deltayi = (1 / 6) * (k1 + 4 * k2 + k3)
    y += deltayi
    return (deltayi, y)

def MakeTable() -> None:
    """Мне уже"""
    pass

def CalculateError() -> None:
    """Просто похуй"""
    pass