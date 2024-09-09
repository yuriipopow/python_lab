import math

def second_task(x: float, y: float) -> float:
    first_polynomial = math.log(pow(x, 3))
    second_polynomial = math.tan(y)
    third_polynomial = pow((x + y), 3)
    fourth_polynomial = (x * math.sin(y + 1.6)) / (177 * pow(x, 2))
    result = first_polynomial + second_polynomial + third_polynomial + fourth_polynomial
    return result

def first_task():
    fruit: str = "banana"
    print(f"This is my favorite fruit: {fruit}")

    score: int = 0
    passing_score:int = 60
    is_good_result: bool = score >= passing_score

    print(f"Is good result: {is_good_result}")

    is_even: bool = False
    is_odd: bool = True

    print(f"Is even: {is_even}")
    print(f"Is odd: {is_odd}")



if __name__ == "__main__":
    first_task()
    result_of_calculate: float = second_task(x=4.123, y=2.395)
    print(result_of_calculate)