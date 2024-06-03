import math

def f(x: float, y: float) -> float:
    """Возвращает правую часть дифференциального уравнения"""
    return y + math.pow(x,2)

def AnalyticSolution(x: float) -> float:
    """Возращает точное аналитическое решение дифференциального 
    уравнения"""
    return -(math.pow(x, 2)) - 2*x + 5*math.exp(x) - 2

def TrueValue(x: list[float], n: float)-> list[float]:
    """Возвращает точное значение в заданых точках x"""
    return [AnalyticSolution(x[i]) for i in range(1, int(n+1))]

def getStep(start_value: float, final_value: float, step: float) ->  float:
    return (final_value - start_value) / step

def getXi(init_val: float, step: float, overall_steps: float) -> list[float]:
    value = init_val
    result = list()
    for _  in range(int(init_val), int(overall_steps + 1)):
        result.append(value)
        value += step
    return result

def CalculateIterations(method:function, x: list[float], y0: float, n: float, h: float) -> list[float]:
    """Считает значение дифференциального уравнения по заданному методу"""
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
    """Считает значение прироста и значение y на одной итерации по методу Эйлера"""
    deltayi = h * f(x,y)
    y += deltayi
    return (deltayi, y)

def ModifiedEulersMethod(x: float, y: float, h: float) -> tuple[float, float]:
    """Считает значение прироста и значение y на одной итерации по модифицированному методу Эйлера"""
    y2 = (h / 2) * f(x,y)
    deltayi = h * f(x + (h / 2), y + y2)
    y += deltayi
    return (deltayi, y)

def RungeKuttasMethod(x: float, y: float, h: float) -> tuple[float, float]:
    """Считает значение прироста и значение y на одной итерации по методу Рунге-Кутта"""
    k1 = h * f(x, y)
    k2 = h * f(x + ( h / 2 ), y + (k1 / 2))
    k3 = h * f(x + h, y + 2 * k2 - k1)
    deltayi = (1 / 6) * (k1 + 4 * k2 + k3)
    y += deltayi
    return (deltayi, y)

def MakeTable(columns: tuple[list[float]]) -> None:
    """Мне уже"""
    pass

def CalculateError(MethodsResults: tuple[list[float]]) -> None:
    """Просто похуй"""
    pass

def main():
    a = 0
    b = 0.5
    y0 = 0
    h = 0.1
    n = getStep(a, b, h)
    x = getXi(a, h, n)
    pass

if __name__ == '__main__':
    main()