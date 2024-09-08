import math


def first_task(h: float, interval: list[float]):
    x: float = interval[0]

    def first_math_function():
        if x > 1:
            return math.log((math.log10(x) + math.log(x, 3)))
        else:
            return "undefined"

    def second_math_function():
        return math.cos(math.sin(pow(x, 2)))

    def third_math_function():
        return math.pow((pow(x, 3) + 0.5), 1 / 7)

    while interval[0] <= x <= interval[1]:
        if x <= 0.4:
            print(f'x = {x} => {first_math_function()}')
        elif 0.4 < x <= 0.6:
            print(f'x = {x} => {second_math_function()}')
        else:
            print(f'x = {x} => {third_math_function()}')
        x += h
        x = math.trunc(x * 100) / 100

def second_task(h: float, interval: list[float], epsilon: float):
    x: float = interval[0]

    def math_function(n: int, x: float) -> float:
        return pow(-1, n + 1) * pow(x, n) / n

    while interval[0] <= x <= interval[1]:
        n: int = 1
        sum_of_expression: float = 0
        term: float = math_function(n, x)
        while abs(term) >= epsilon:
            sum_of_expression += term
            n += 1
            term = math_function(n, x)
        print(f'x = {x} => {sum_of_expression}')
        x += h
        x = math.trunc(x * 100) / 100

if __name__ == '__main__':
    second_task(0.05, [0.1, 0.5], 0.001)
