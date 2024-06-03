import math


def f(x: float, y: float) -> float:
    """Возвращает правую часть дифференциального уравнения"""
    return (1/2) * math.sin(2 * x) - (y * math.cos(x))


def analytic_solution(x: float) -> float:
    """Возращает точное аналитическое решение дифференциального 
    уравнения"""
    return math.sin(x) + (1 / math.pow(math.e, math.sin(x))) - 1


def true_value(x: list[float], n: float) -> list[float]:
    """Возвращает точное значение в заданых точках x"""
    return [analytic_solution(x[i]) for i in range(0, int(n+1))]


def get_step(start_value: float, final_value: float, step: float) -> float:
    """Рассчитывает количество шагов разбиения"""
    return (final_value - start_value) / step


def get_x(init_val: float, step: float, overall_steps: float) -> list[float]:
    """Рассчитывает точки x по заданному разбиению"""
    value = init_val
    result = list()
    for _ in range(int(init_val), int(overall_steps + 1)):
        result.append(value)
        value += step
    return result


def calculate(method, x: list[float], y0: float, n: float, h: float,
              create_table: bool = False) -> list[float]:
    """Считает значение дифференциального уравнения по заданному методу"""
    y = [y0]
    deltayi = list()
    for i in range(0, int(n)):
        result = method(x[i], y[i], h)
        deltayi.append(result[0])
        y.append(result[1])
    deltayi.append(0)
    if create_table:
        make_table((x, y, deltayi, ))
    return y


def eulers_method(x: float, y: float, h: float) -> tuple[float, float]:
    """Считает значение прироста \
        и значение y на одной итерации по методу Эйлера"""
    deltayi = h * f(x, y)
    y += deltayi
    return (deltayi, y)


def modified_eulers_method(x: float, y: float, h: float) -> tuple[float, float]:
    """Считает значение прироста и \
        значение y на одной итерации по модифицированному методу Эйлера"""
    y2 = (h / 2) * f(x, y)
    deltayi = h * f(x + (h / 2), y + y2)
    y += deltayi
    return (deltayi, y)


def runge_kuttas_method(x: float, y: float, h: float) -> tuple[float, float]:
    """Считает значение прироста и значение y на одной итерации по методу Рунге-Кутта"""
    k1 = h * f(x, y)
    k2 = h * f(x + (h / 2), y + (k1 / 2))
    k3 = h * f(x + (h / 2), y + (k2 / 2))
    k4 = h * f(x + h, y + k3)
    deltayi = (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    y += deltayi
    return (deltayi, y)


def make_table(columns: tuple[list[float], ...], precision: int = 4) -> None:
    """Печатает таблицу в формате (iteration, x, y, deltay)"""
    float_precision = f"%.{int(precision)}f"
    header = "i\tx\ty\tdelta y"
    print(header)
    for i in range(0, len(columns[0])):
        buf = f"{i}\t"
        for j in range(0, len(columns)):
            buf += f"{float_precision % columns[j][i]}\t"
        print(buf)


def calculate_error(values: tuple[list[float]],
                    x: list[float],
                    precision: int = 4) -> None:
    """Создает и печатает таблицу погрешностей"""
    exponent_precision: str = "%.2e"
    float_precision: str = f"%.{precision}f"
    for value in values:
        value.pop(0)
    x.pop(0)

    header = "\nx\t\t\tТочное решение\tМетод Эйлера\tМетод Эйлера(М)\tМетод Рунге-Кутта"
    print(header)
    for i in range(len(x)):
        buf = f"{float_precision % x[i]}\t\t\t"
        for j in range(len(values)):
            buf += f"{float_precision % values[j][i]}\t\t"
        print(buf)
    footer = f"Погрешность x={x[-1]}:\t"
    for i in range(len(values)):
        footer += f"{exponent_precision %
                     abs(values[i][-1] - values[0][-1])}\t"
    print(footer)


def main():
    a = 0
    b = 1
    y0 = 0
    h = 0.2
    n = get_step(a, b, h)
    x = get_x(a, h, n)

    print(x)

    print("\nМетод Эйлера:\n")
    y_e = calculate(eulers_method, x, y0, n, h, True)
    print("\nМодифицированный метод Эйлера:\n")
    y_me = calculate(modified_eulers_method, x, y0, n, h, True)
    print("\nМетод Рунге-Кутта:\n")
    y_rk = calculate(runge_kuttas_method, x, y0, n, h, True)
    y_t = true_value(x, n)
    calculate_error((y_t, y_e, y_me, y_rk), x)


if __name__ == '__main__':
    main()
