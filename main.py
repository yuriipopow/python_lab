import math
from typing import Optional

def first_task(h: float, interval: list[float]):
    x: float = interval[0]

    def first_math_function() -> Optional[float]:
        if x > 1:
            return math.log((math.log10(x) + math.log(x, 3)))
        else:
            return None

    def second_math_function() -> float:
        return math.cos(math.sin(pow(x, 2)))

    def third_math_function() -> float:
        return math.pow((pow(x, 3) + 0.5), 1 / 7)

    while interval[0] <= x <= interval[1]:
        if x <= 0.4:
            print(f'x = {x} => {first_math_function()}')
        elif 0.4 < x <= 0.6:
            print(f'x = {x} => {second_math_function()}')
        else:
            print(f'x = {x} => {third_math_function()}')
        x += h
        x = round(x, 2)


def second_task(h: float, interval: list[float], d: float):
    x = interval[0]

    def math_function(n_num: int, x_num: float) -> float:
        return pow(-1, n_num) * (pow(x_num, n_num) / n_num)

    while x <= interval[1]:
        sum_value: float = 0
        n: int = 1
        term: float = math_function(n, x)

        while abs(term) >= d:
            sum_value += term
            n += 1
            term = math_function(n, x)

        print(f"{x}, S(x) = {sum_value}")
        x += h
        x = round(x, 2)













if __name__ == '__main__':
    # first_task(0.1, [0.1, 0.5])
    second_task(0.05, [0.1, 0.5], 0.0001000001)
