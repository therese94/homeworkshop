import math

def my_sqrt(n):
    x, y = 1, n
    result = 1  # 우리가 추측하는 제곱근

    while abs(result ** 2 -n ) > 0.00000001:
        result = (x + y) / 2
        if result ** 2 < n :
            x = result
        else:
            y = result

    return result