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
    return [AnalyticSolution(x[i]) for i in range(0, int(n+1))]

def getStep(start_value: float, final_value: float, step: float) ->  float:
    return (final_value - start_value) / step

def getX(init_val: float, step: float, overall_steps: float) -> list[float]:
    value = init_val
    result = list()
    for _  in range(int(init_val), int(overall_steps + 1)):
        result.append(value)
        value += step
    return result

def Calculate(method, x: list[float], y0: float, n: float, h: float, makeTable: bool = False) -> list[float]:
    """Считает значение дифференциального уравнения по заданному методу"""
    y = [y0]
    deltayi = list()

    for i in range(0, int(n)):
        result = method(x[i], y[i], h)
        deltayi.append(result[0])
        y.append(result[1])

    deltayi.append(0)
    if makeTable:
        MakeTable((x, y, deltayi))
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

def MakeTable(columns: tuple[list[float]], precision: int = 4) -> None:
    """Печатает таблицу в формате (iteration, x, y, deltay)"""
    precision = f"%.{int(precision)}f"
    header = "i\tx\ty\tdelta y"
    print(header)
    for i in range(0, len(columns[0])):
        buf = f"{i}\t"
        for j in range(0, len(columns)):
            buf += f"{precision % columns[j][i]}\t"
        print(buf)

def CalculateError(values: tuple[list[float]], x: list[float], precision: int = 4) -> None:
    """Создает и печатает таблицу погрешностей"""
    exponent_precision = "%.2e"
    precision = f"%.{int(precision)}f"
    for value in values:
        value.pop(0)
    x.pop(0)
    
    header = "x\t\tТочное решение\tМетод Эйлера\tМетод Эйлера(М)\tМетод Рунге-Кутта"
    print(header)
    for i in range(len(x)):
        buf = f"{precision % x[i]}\t\t"
        for j in range(len(values)):
            buf += f"{precision % values[j][i]}\t\t"
        print(buf)
    footer = f"Погрешность x={x[-1]}: "
    for i in range(len(values)):
        footer += f"{exponent_precision % abs(values[i][-1] - values[0][-1])}\t"
    print(footer)
    pass

def main():
    a = 0
    b = 0.5
    y0 = 3
    h = 0.1
    n = getStep(a, b, h)
    x = getX(a, h, n)

    print("\nМетод Эйлера:\n")
    y_E = Calculate(EulersMethod, x, y0, n, h, True)
    print("\nМодифицированный метод Эйлера:\n")
    y_mE = Calculate(ModifiedEulersMethod, x, y0, n, h, True)
    print("\nМетод Рунге-Кутта:\n")
    y_RK = Calculate(RungeKuttasMethod, x, y0, n, h, True)
    y_T = TrueValue(x,n)
    print("\n")
    CalculateError((y_T, y_E, y_mE, y_RK), x)

    

if __name__ == '__main__':
    main()